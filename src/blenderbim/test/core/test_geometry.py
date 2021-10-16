# BlenderBIM Add-on - OpenBIM Blender Add-on
# Copyright (C) 2021 Dion Moult <dion@thinkmoult.com>
#
# This file is part of BlenderBIM Add-on.
#
# BlenderBIM Add-on is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BlenderBIM Add-on is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BlenderBIM Add-on.  If not, see <http://www.gnu.org/licenses/>.

import blenderbim.core.geometry as subject
from test.core.bootstrap import ifc, surveyor


class TestEditObjectPlacement:
    def test_run(self, ifc, surveyor):
        ifc.get_entity("obj").should_be_called().will_return("element")
        surveyor.get_absolute_matrix("obj").should_be_called().will_return("matrix")
        ifc.run("geometry.edit_object_placement", product="element", matrix="matrix").should_be_called()
        subject.edit_object_placement(ifc, surveyor, obj="obj")