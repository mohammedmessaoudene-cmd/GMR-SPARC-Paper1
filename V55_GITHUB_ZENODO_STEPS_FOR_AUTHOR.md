# V55 GitHub and Zenodo Steps for Author

The local package is ready after repository metadata only. Complete these steps before journal upload.

## 1. Create the public GitHub repository

1. Create a public repository, for example `GMR-SPARC-Paper1`.
2. Upload the contents of `GMR-SPARC-Paper1_REPOSITORY_RELEASE_V55.zip` or push the extracted repository folder.
3. Confirm that the public repository includes `README.md`, `REPRODUCE.md`, `METHOD_FILES.md`, `CITATION.cff`, `scripts/`, `tables/`, `source_csv/`, `figures/`, and manuscript source files.
4. Create a release tag, preferably `v1.0.0`.

## 2. Archive the release

1. Connect the GitHub repository to Zenodo or OSF.
2. Archive the `v1.0.0` release.
3. Record the permanent DOI.

## 3. Insert final metadata

Replace the placeholders in:

- `CITATION.cff`
- Manuscript Data Availability section
- `README.md`
- Submission checklist

Use this wording in the manuscript once both records are real:

`The SPARC input data are publicly available from the SPARC database. The derived analysis products, radial diagnostic tables, figure-source files, and reproduction scripts are archived at [DOI] and developed at [GitHub URL].`

## 4. Recompile and repackage

After inserting real metadata, recompile the manuscript and supplement, then create final upload packages. Only then may the final verdict become:

`APJ_V55_READY_TO_SUBMIT`
