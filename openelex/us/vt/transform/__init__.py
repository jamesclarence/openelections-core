from transforms import *
from openelex.base.transform import Transform, registry

registry.register('vt', CreateContestsTransform)
registry.register('vt', CreateCandidates)
registry.register('vt', CreateResultsTransform)
