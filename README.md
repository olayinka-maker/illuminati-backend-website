# Contact API (FastAPI)

Simple backend to collect form data and serve it as JSON for your frontend.

## Files

- [main.py](main.py) — FastAPI application with endpoints
- [models.py](models.py) — SQLAlchemy ORM `Contact` model
- [schemas.py](schemas.py) — Pydantic request/response schemas
- [database.py](database.py) — SQLite engine and session factory

## Install

Create a virtualenv and install:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload --port 8000
```

The API will be at `http://127.0.0.1:8000` and docs at `http://127.0.0.1:8000/docs`.

## Endpoints

- `POST /contacts/` — create a contact (JSON body)
- `GET /contacts/` — list contacts
- `GET /contacts/{id}` — get single contact

## Example frontend (submit form)

Use fetch to POST the form JSON to the API. Example mapping assumes your form inputs have `id` attributes matching keys.

```html
<script>
async function submitForm() {
  const body = {
    full_name: document.getElementById('full_name').value,
    email: document.getElementById('email').value,
    country: document.getElementById('country').value,
    state_of_origin: document.getElementById('state_of_origin').value,
    date_of_birth: document.getElementById('date_of_birth').value,
    age: document.getElementById('age').value,
    occupation: document.getElementById('occupation').value,
    income: document.getElementById('income').value,
    gender: document.getElementById('gender').value,
    phone_number: document.getElementById('phone_number').value,
    address: document.getElementById('address').value,
    how_hear: document.getElementById('how_hear').value,
    about: document.getElementById('about').value
  };

  const res = await fetch('http://127.0.0.1:8000/contacts/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });

  const data = await res.json();
  console.log('created', data);
}
</script>
```

## Example frontend (populate form from API)

```html
<script>
async function populate(contactId) {
  const res = await fetch(`http://127.0.0.1:8000/contacts/${contactId}`);
  const c = await res.json();
  document.getElementById('full_name').value = c.full_name || '';
  document.getElementById('email').value = c.email || '';
  document.getElementById('country').value = c.country || '';
  document.getElementById('state_of_origin').value = c.state_of_origin || '';
  document.getElementById('date_of_birth').value = c.date_of_birth || '';
  document.getElementById('age').value = c.age || '';
  document.getElementById('occupation').value = c.occupation || '';
  document.getElementById('income').value = c.income || '';
  document.getElementById('gender').value = c.gender || '';
  document.getElementById('phone_number').value = c.phone_number || '';
  document.getElementById('address').value = c.address || '';
  document.getElementById('how_hear').value = c.how_hear || '';
  document.getElementById('about').value = c.about || '';
}
</script>
```

## Notes

- The API uses a local SQLite DB (`contacts.db`) created automatically.
- CORS is enabled for development; restrict `allow_origins` for production.
