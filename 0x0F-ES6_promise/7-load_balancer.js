export default async function loadBalancer(chinaDownload, USDownload) {
  const downloads = [chinaDownload, USDownload];
  try {
    return await Promise.any(downloads);
  } catch (error) {
    throw new Error(`All downloads failed: ${error.message}`);
  }
}
