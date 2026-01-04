import "dotenv/config";
import { createClient } from "@supabase/supabase-js";
import fs from "fs";
import path from "path";

const PDF_DIR = "../01_Pdf_original";
const MAPS_DIR = "../03_Maps";
const STORAGE_BUCKET = "legal_acts";

export const supabase = createClient(
  process.env.SUPABASE_URL || "http://localhost:8000",
  process.env.SUPABASE_KEY ||
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICAgInJvbGUiOiAic2VydmljZV9yb2xlIiwKICAgICJpc3MiOiAic3VwYWJhc2UiLAogICAgImlhdCI6IDE2ODI1NDY0MDAsCiAgICAiZXhwIjogMTg0MDM5OTIwMAp9.4JNHcZE4PiBqI6n41t4vppx7lIsZSHiCRJXUjxDey3c"
);

async function uploadPdfAndUpdatePath(filePath, legalActId) {
  const fileBuffer = fs.readFileSync(filePath);
  const fileName = path.basename(filePath);

  // Upload to Supabase storage
  const { data: uploadData, error: uploadError } = await supabase.storage
    .from(STORAGE_BUCKET)
    .upload(fileName, fileBuffer, {
      contentType: "application/pdf",
      upsert: true,
    });

  if (uploadError) {
    throw new Error(`Upload error: ${uploadError.message}`);
  }

  const pdfPath = `/${fileName}`;

  // Update legal_acts table
  const { error: updateError } = await supabase
    .from("legal_acts")
    .update({ pdf_path: pdfPath })
    .eq("id", legalActId);

  if (updateError) {
    throw new Error(`Update error: ${updateError.message}`);
  }

  return pdfPath;
}

async function updatePdfMap(mapFilePath, legalActId) {
  const mapContent = JSON.parse(fs.readFileSync(mapFilePath, "utf-8"));

  const { error: updateError } = await supabase
    .from("legal_acts")
    .update({ pdf_map: mapContent })
    .eq("id", legalActId);

  if (updateError) {
    throw new Error(`Update map error: ${updateError.message}`);
  }
}

async function processFiles() {
  try {
    // Process PDFs
    const pdfFiles = fs
      .readdirSync(PDF_DIR)
      .filter((file) => file.endsWith(".pdf"));

    console.log(`Found ${pdfFiles.length} PDF files to process`);

    for (const pdfFile of pdfFiles) {
      const legalActId = path.basename(pdfFile, ".pdf");
      const filePath = path.join(PDF_DIR, pdfFile);

      try {
        const pdfPath = await uploadPdfAndUpdatePath(filePath, legalActId);
        console.log(`Uploaded and updated ${legalActId}: ${pdfPath}`);
      } catch (e) {
        console.error(`Error processing PDF ${pdfFile}:`, e.message);
      }
    }

    // Process Maps
    const mapFiles = fs
      .readdirSync(MAPS_DIR)
      .filter((file) => file.endsWith("_map.json"));

    console.log(`Found ${mapFiles.length} map files to process`);

    for (const mapFile of mapFiles) {
      const legalActId = path.basename(mapFile, "_map.json");
      const filePath = path.join(MAPS_DIR, mapFile);

      try {
        await updatePdfMap(filePath, legalActId);
        console.log(`Updated map for ${legalActId}`);
      } catch (e) {
        console.error(`Error processing map ${mapFile}:`, e.message);
      }
    }

    console.log("Processing complete!");
  } catch (error) {
    console.error("Error occurred:", error);
  }
}

processFiles();
