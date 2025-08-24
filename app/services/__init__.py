from .alumno_service import AlumnoService
from .area_service import AreaService
from .autoridad_service import AutoridadService
from .cargo_service import CargoService
from .categoria_cargo_service import CategoriaCargoService
from .departamento_service import DepartamentoService
from .documentos_office_service import PDFDocument, ODTDocument, DOCXDocument
from .especialidad_service import EspecialidadService
from .facultad_service import FacultadService
from .grado_service import GradoService
from .grupo_service import GrupoService
from .inscripcion_service import InscripcionService
from .materia_service import MateriaService
from .orientacion_service import OrientacionService
from .plan_service import PlanService
from .tipo_documento_service import TipoDocumentoService
from .universidad_service import UniversidadService

__all__ = [
    "AlumnoService",
    "AreaService",
    "AutoridadService",
    "CargoService",
    "CategoriaCargoService",
    "DepartamentoService",
    "PDFDocument",
    "ODTDocument",
    "DOCXDocument",
    "EspecialidadService",
    "FacultadService",
    "GradoService",
    "GrupoService",
    "InscripcionService",
    "MateriaService",
    "OrientacionService",
    "PlanService",
    "TipoDocumentoService",
    "UniversidadService",
]
