# Marine Biodiversity Mapping

A Django-based application for mapping marine biodiversity, featuring spatial data support via GeoDjango and Django Rest Framework GIS.

## Prerequisites

- Python 3.10+ (Python 3.14 supported)
- GDAL (Geospatial Data Abstraction Library)
- SQLite (default) or PostgreSQL/PostGIS (optional)

## Installation

1. **Clone the repository**

2. **Create and activate a virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Install GDAL (Windows users only)**
   
   > **Note:** Just running `pip install GDAL` will likely fail on Windows as it requires compilation tools.

   You need to install a pre-compiled binary wheel for GDAL that matches your Python version.
   
   **For Python 3.14:**
   Download the wheel from [cgohlke/geospatial-wheels](https://github.com/cgohlke/geospatial-wheels/releases) (e.g., `GDAL-3.11.4-cp314-cp314-win_amd64.whl`).
   
   Then install it:
   ```powershell
   pip install path\to\GDAL-3.11.4-cp314-cp314-win_amd64.whl
   ```
   
   **Alternatively (conda):**
   ```powershell
   conda install -c conda-forge gdal
   ```

## Configuration

The project is configured to automatically detect GDAL if installed in the virtual environment (common with wheel installations) or if `OSGEO4W` is used.

If you encounter `ImproperlyConfigured: Could not find the GDAL library`, ensure GDAL is installed and, if necessary, set the `GDAL_LIBRARY_PATH` environment variable.

## Running the Application

1. **Apply Migrations**
   ```powershell
   python manage.py migrate
   ```

2. **Start the Development Server**
   ```powershell
   python manage.py runserver
   ```

   The API will be available at `http://localhost:8000/`.

## API Documentation

- **Species API**: `/api/species/`
- **Reef Sites API**: `/api/reefs/`
