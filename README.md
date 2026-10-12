# Fight For Life · injured-animal rescue alerts

A web app that helps a passer-by get help to an injured animal fast. You upload a photo of the animal,
the app records where it was taken, and the report is routed to nearby NGOs and vets.
Built at Manipal University Jaipur (2023) by Yuvraj Chawla, Ananya Bhardwaj and Tanash Sultania.

## What is in this repository

| Path | What it is |
| --- | --- |
| `web/` | The public site: home, about and contact pages (HTML, CSS, vanilla JS) |
| `app/app.py` | Flask backend: photo upload, SQLite storage and geolocation of each report |
| `app/templates/index.html` | Upload form and list of reported cases |

The species and condition classifier (a TinyVGG convolutional network trained on photos of dogs and cows)
was trained separately and is not part of this repository yet. Site imagery and team photos are left out
for licensing and privacy reasons, so some images on the static pages will not load.

## Run the backend

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app/app.py           # http://127.0.0.1:5000
```

## Roadmap

- Bring the TinyVGG classifier into the upload flow so each report is tagged with species and severity
- Read GPS coordinates from the photo's EXIF data instead of geocoding the file name
- Notify the nearest registered NGO or vet by email or SMS

MIT License.
