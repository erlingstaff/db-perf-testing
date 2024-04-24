from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Select


def test_enum_all_asdict(crsresults):
    return [row._asdict() for _, row in enumerate(crsresults.all())]

def test_all_asdict(crsresults):
    return [row._asdict() for row in crsresults.all()]

def test_mappings(crsresults):
    return crsresults.mappings()

def test_all(crsresults):
    return crsresults.all()

def test_scalars(crsresults):
    return crsresults.scalars()

def test_mappings_all(crsresults):
    return crsresults.mappings().all()

def test_scalars_all(crsresults):
    return crsresults.scalars().all()

def get_cursorresults(limit, table_num):
    engine = create_engine("postgresql+psycopg2://rucio:secret@localhost/rucio")
    metadata = MetaData(schema="dev")

    tables = {i: Table(f"test_table{i}", metadata, autoload_with=engine) for i in range(7)}

    with engine.connect() as conn:
        res = conn.execute(Select(tables[table_num]).limit(limit))
        return res
