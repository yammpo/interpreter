
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD_END ADD_START AND_END AND_START ASSIGN_END ASSIGN_START BOOL CALL_END CALL_START CELL CHECK_END CHECK_START CONDITION_END CONDITION_START CONST COUNT DIMENSIONS_END DIMENSIONS_START DIMENSION_END DIMENSION_START DIM_END DIM_START DIV_END DIV_START DOWN_END DOWN_START DO_END DO_START EMPTY EQUALSIGN EQ_END EQ_START EXIT FALSE FUNC_END FUNC_START GETDRONSCOUNT_END GETDRONSCOUNT_START ID INDEX_END INDEX_START INT LBRACKET LEFT_END LEFT_START MAIN MAX_END MAX_START MIN_END MIN_START MUL_END MUL_START NAME NOT_END NOT_START NUMBER OR_END OR_START PROGRAM_END PROGRAM_START RBRACKET RIGHT_END RIGHT_START SENDDRONS_END SENDDRONS_START SUB_END SUB_START SWITCH_END SWITCH_START TO_END TO_START TRUE TYPE_END TYPE_START UNDEF UP_END UP_START VALUES_END VALUES_START VALUE_END VALUE_START VARDECLARATION_END VARDECLARATION_START VAR_END VAR_START WALL WHILE_END WHILE_STARTprogram : PROGRAM_START blocks PROGRAM_ENDblocks : blocks block\n\t\t| blockblock : vardeclaration\n\t\t| function\n\t\t| emptyblock : errorfunction : FUNC_START NAME EQUALSIGN funcname RBRACKET statements FUNC_ENDstatements : statements statement\n\t\t| statementstatement : vardeclaration\n\t\t| assignment \n\t\t| while\n\t\t| switch\n\t\t| call\n\t\t| operator\n\t\t| emptystatement : errorassignment : ASSIGN_START VALUE_START expression VALUE_END TO_START variables TO_END ASSIGN_ENDwhile : WHILE_START CHECK_START expression CHECK_END DO_START statements DO_END WHILE_ENDswitch : SWITCH_START conditions SWITCH_ENDconditions : conditions condition\n\t\t| conditioncondition : CONDITION_START CHECK_START expression CHECK_END DO_START statements DO_END CONDITION_END\n\t\t| emptycondition : errorcall : CALL_START funcname CALL_ENDfuncname : ID\n\t\t| MAINvardeclaration : VARDECLARATION_START declarations VARDECLARATION_ENDdeclarations : declarations declaration\n\t\t| declarationdeclaration : declaration_var\n\t\t| declaration_var_init\n\t\t| declaration_var_const\n\t\t| declaration_array\n\t\t| declaration_array_init\n\t\t| declaration_array_const\n\t\t| emptydeclaration_var : VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END LBRACKET VAR_END\n\t\t| VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END LBRACKET VAR_ENDdeclaration_var_const : VAR_START EQUALSIGN id CONST EQUALSIGN TRUE RBRACKET TYPE_START type TYPE_END VALUE_START expression VALUE_END LBRACKET VAR_ENDdeclaration_var_init : VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END VALUE_START expression VALUE_END LBRACKET VAR_END\n\t\t| VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END VALUE_START expression VALUE_END LBRACKET VAR_ENDdeclaration_array : VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END LBRACKET VAR_END\n\t\t| VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END LBRACKET VAR_ENDdeclaration_array_init : VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END VALUES_START values VALUES_END LBRACKET VAR_END\n\t\t| VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END VALUES_START values VALUES_END LBRACKET VAR_ENDdeclaration_array_const : VAR_START EQUALSIGN id CONST EQUALSIGN TRUE RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END VALUES_START values VALUES_END LBRACKET VAR_ENDvalues : values value\n\t\t| valuevalue : VALUE_START expression VALUE_ENDdimensions : dimensions dimension\n\t\t| dimensiondimension : DIMENSION_START expression DIMENSION_ENDtype : INT\n\t\t| CELL\n\t\t| BOOLid : IDvariables : variables variable\n\t\t| variablevariable : VAR_START NAME EQUALSIGN id VAR_END\n\t\t| VAR_START NAME EQUALSIGN id RBRACKET DIM_START indexes DIM_END LBRACKET VAR_END\n\t\t| emptyindexes : indexes index\n\t\t| indexindex : INDEX_START expression INDEX_ENDexpressions : expressions expression\n\t\t| expressionexpression : variable\n\t\t| const\n\t\t| math\n\t\t| emptyconst : TRUE\n\t\t| FALSE\n\t\t| NUMBER\n\t\t| EMPTY\n\t\t| WALL\n\t\t| EXIT\n\t\t| UNDEFmath : ADD_START expressions ADD_END\n\t\t| MUL_START expressions MUL_END\n\t\t| SUB_START expressions SUB_END\n\t\t| DIV_START expressions DIV_END\n\t\t| OR_START expressions OR_END\n\t\t| AND_START expressions AND_END\n\t\t| MAX_START expressions MAX_END\n\t\t| MIN_START expressions MIN_END\n\t\t| EQ_START expressions EQ_END\n\t\t| NOT_START expression NOT_ENDoperator : LEFT_START expression LEFT_END\n\t\t| RIGHT_START expression RIGHT_END\n\t\t| UP_START expression UP_END\n\t\t| DOWN_START expression DOWN_END\n\t\t| SENDDRONS_START expression SENDDRONS_END\n\t\t| GETDRONSCOUNT_START variable GETDRONSCOUNT_ENDempty : '
    
_lr_action_items = {'PROGRAM_START':([0,],[2,]),'$end':([1,11,],[0,-1,]),'error':([2,3,4,5,6,7,8,12,24,35,38,39,40,41,42,43,44,45,46,47,50,64,65,68,69,71,72,108,109,111,112,125,126,127,128,129,156,165,166,179,188,189,201,],[8,8,-3,-4,-5,-6,-7,-2,-30,47,47,-10,-11,-12,-13,-14,-15,-16,-17,-18,72,-8,-9,72,-23,-25,-26,-21,-22,-27,-91,-92,-93,-94,-95,-96,47,47,47,47,-19,-20,-24,]),'VARDECLARATION_START':([2,3,4,5,6,7,8,12,24,35,38,39,40,41,42,43,44,45,46,47,64,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[9,9,-3,-4,-5,-6,-7,-2,-30,9,9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-8,-9,-21,-27,-91,-92,-93,-94,-95,-96,9,9,9,9,-19,-20,]),'FUNC_START':([2,3,4,5,6,7,8,12,24,64,],[10,10,-3,-4,-5,-6,-7,-2,-30,-8,]),'PROGRAM_END':([2,3,4,5,6,7,8,12,24,64,],[-97,11,-3,-4,-5,-6,-7,-2,-30,-8,]),'VAR_START':([9,13,14,15,16,17,18,19,20,21,25,52,53,54,55,56,57,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,102,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,150,155,163,164,167,172,174,177,181,183,193,196,217,219,221,222,225,238,239,246,247,],[22,22,-32,-33,-34,-35,-36,-37,-38,-39,-31,79,79,79,79,79,79,79,79,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,79,79,79,79,79,79,79,79,79,79,-64,79,79,-69,79,79,79,79,79,79,79,79,79,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-40,79,79,-61,-62,79,79,-60,-43,-41,79,79,-44,-42,-63,-45,79,-47,-46,-48,-49,]),'VARDECLARATION_END':([9,13,14,15,16,17,18,19,20,21,25,150,181,183,217,219,222,238,239,246,247,],[-97,24,-32,-33,-34,-35,-36,-37,-38,-39,-31,-40,-43,-41,-44,-42,-45,-47,-46,-48,-49,]),'NAME':([10,79,],[23,113,]),'EQUALSIGN':([22,23,34,113,152,185,187,],[26,27,37,138,160,198,200,]),'FUNC_END':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,188,189,],[-30,-97,64,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,-19,-20,]),'ASSIGN_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,48,48,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,48,48,48,48,-19,-20,]),'WHILE_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,49,49,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,49,49,49,49,-19,-20,]),'SWITCH_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,50,50,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,50,50,50,50,-19,-20,]),'CALL_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,51,51,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,51,51,51,51,-19,-20,]),'LEFT_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,52,52,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,52,52,52,52,-19,-20,]),'RIGHT_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,53,53,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,53,53,53,53,-19,-20,]),'UP_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,54,54,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,54,54,54,54,-19,-20,]),'DOWN_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,55,55,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,55,55,55,55,-19,-20,]),'SENDDRONS_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,56,56,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,56,56,56,56,-19,-20,]),'GETDRONSCOUNT_START':([24,35,38,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,57,57,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,57,57,57,57,-19,-20,]),'DO_END':([24,39,40,41,42,43,44,45,46,47,65,108,111,112,125,126,127,128,129,156,165,166,179,188,189,],[-30,-10,-11,-12,-13,-14,-15,-16,-17,-18,-9,-21,-27,-91,-92,-93,-94,-95,-96,-97,178,-97,190,-19,-20,]),'ID':([26,27,51,138,],[29,31,31,29,]),'MAIN':([27,51,],[32,32,]),'RBRACKET':([28,29,30,31,32,62,63,80,81,82,83,84,85,86,158,170,209,211,],[33,-59,35,-28,-29,104,105,-74,-75,-76,-77,-78,-79,-80,168,182,218,220,]),'CONST':([28,29,],[34,-59,]),'VAR_END':([29,130,158,169,171,208,210,212,214,233,235,244,245,],[-59,150,167,181,183,217,219,221,222,238,239,246,247,]),'CALL_END':([31,32,73,],[-28,-29,111,]),'TYPE_START':([33,104,105,],[36,133,134,]),'INT':([36,133,134,],[59,59,59,]),'CELL':([36,133,134,],[60,60,60,]),'BOOL':([36,133,134,],[61,61,61,]),'FALSE':([37,52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,160,167,172,174,193,196,198,200,221,225,],[62,81,81,81,81,81,81,81,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,81,81,81,81,81,81,81,81,81,81,81,81,-69,81,81,81,81,81,81,81,81,81,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,81,-62,81,81,81,81,81,81,-63,81,]),'TRUE':([37,52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,160,167,172,174,193,196,198,200,221,225,],[63,80,80,80,80,80,80,80,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,80,80,80,80,80,80,80,80,80,80,80,80,-69,80,80,80,80,80,80,80,80,80,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,80,-62,80,80,80,80,80,80,-63,80,]),'VALUE_START':([48,103,161,162,215,223,224,229,234,236,237,240,241,],[66,131,172,174,225,225,-51,-50,-52,225,225,225,225,]),'CHECK_START':([49,70,],[67,110,]),'CONDITION_START':([50,68,69,71,72,109,201,],[70,70,-23,-25,-26,-22,-24,]),'SWITCH_END':([50,68,69,71,72,109,201,],[-97,108,-23,-25,-26,-22,-24,]),'NUMBER':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,160,167,172,174,193,196,198,200,221,225,],[82,82,82,82,82,82,82,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,82,82,82,82,82,82,82,82,82,82,82,82,-69,82,82,82,82,82,82,82,82,82,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,82,-62,82,82,82,82,82,82,-63,82,]),'EMPTY':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,160,167,172,174,193,196,198,200,221,225,],[83,83,83,83,83,83,83,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,83,83,83,83,83,83,83,83,83,83,83,83,-69,83,83,83,83,83,83,83,83,83,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,83,-62,83,83,83,83,83,83,-63,83,]),'WALL':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,160,167,172,174,193,196,198,200,221,225,],[84,84,84,84,84,84,84,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,84,84,84,84,84,84,84,84,84,84,84,84,-69,84,84,84,84,84,84,84,84,84,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,84,-62,84,84,84,84,84,84,-63,84,]),'EXIT':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,160,167,172,174,193,196,198,200,221,225,],[85,85,85,85,85,85,85,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,85,85,85,85,85,85,85,85,85,85,85,85,-69,85,85,85,85,85,85,85,85,85,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,85,-62,85,85,85,85,85,85,-63,85,]),'UNDEF':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,160,167,172,174,193,196,198,200,221,225,],[86,86,86,86,86,86,86,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,86,86,86,86,86,86,86,86,86,86,86,86,-69,86,86,86,86,86,86,86,86,86,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,86,-62,86,86,86,86,86,86,-63,86,]),'ADD_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[87,87,87,87,87,87,87,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,87,87,87,87,87,87,87,87,87,87,87,87,-69,87,87,87,87,87,87,87,87,87,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,87,87,87,87,-63,87,]),'MUL_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[88,88,88,88,88,88,88,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,88,88,88,88,88,88,88,88,88,88,88,88,-69,88,88,88,88,88,88,88,88,88,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,88,88,88,88,-63,88,]),'SUB_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[89,89,89,89,89,89,89,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,89,89,89,89,89,89,89,89,89,89,89,89,-69,89,89,89,89,89,89,89,89,89,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,89,89,89,89,-63,89,]),'DIV_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[90,90,90,90,90,90,90,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,90,90,90,90,90,90,90,90,90,90,90,90,-69,90,90,90,90,90,90,90,90,90,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,90,90,90,90,-63,90,]),'OR_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[91,91,91,91,91,91,91,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,91,91,91,91,91,91,91,91,91,91,91,91,-69,91,91,91,91,91,91,91,91,91,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,91,91,91,91,-63,91,]),'AND_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[92,92,92,92,92,92,92,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,92,92,92,92,92,92,92,92,92,92,92,92,-69,92,92,92,92,92,92,92,92,92,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,92,92,92,92,-63,92,]),'MAX_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[93,93,93,93,93,93,93,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,93,93,93,93,93,93,93,93,93,93,93,93,-69,93,93,93,93,93,93,93,93,93,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,93,93,93,93,-63,93,]),'MIN_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[94,94,94,94,94,94,94,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,94,94,94,94,94,94,94,94,94,94,94,94,-69,94,94,94,94,94,94,94,94,94,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,94,94,94,94,-63,94,]),'EQ_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[95,95,95,95,95,95,95,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,95,95,95,95,95,95,95,95,95,95,95,95,-69,95,95,95,95,95,95,95,95,95,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,95,95,95,95,-63,95,]),'NOT_START':([52,53,54,55,56,66,67,75,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,110,114,115,116,117,118,119,120,121,122,123,131,139,140,141,142,143,144,145,146,147,148,149,167,172,174,193,196,221,225,],[96,96,96,96,96,96,96,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,96,96,96,96,96,96,96,96,96,96,96,96,-69,96,96,96,96,96,96,96,96,96,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,96,96,96,96,-63,96,]),'LEFT_END':([52,74,75,76,77,78,80,81,82,83,84,85,86,139,141,142,143,144,145,146,147,148,149,167,221,],[-97,112,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'RIGHT_END':([53,75,76,77,78,80,81,82,83,84,85,86,97,139,141,142,143,144,145,146,147,148,149,167,221,],[-97,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,125,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'UP_END':([54,75,76,77,78,80,81,82,83,84,85,86,98,139,141,142,143,144,145,146,147,148,149,167,221,],[-97,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,126,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'DOWN_END':([55,75,76,77,78,80,81,82,83,84,85,86,99,139,141,142,143,144,145,146,147,148,149,167,221,],[-97,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,127,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'SENDDRONS_END':([56,75,76,77,78,80,81,82,83,84,85,86,100,139,141,142,143,144,145,146,147,148,149,167,221,],[-97,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,128,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'GETDRONSCOUNT_END':([57,101,102,167,221,],[-97,129,-64,-62,-63,]),'TYPE_END':([58,59,60,61,153,154,],[103,-56,-57,-58,161,162,]),'VALUE_END':([66,75,76,77,78,80,81,82,83,84,85,86,106,131,139,141,142,143,144,145,146,147,148,149,151,167,172,174,184,186,221,225,230,],[-97,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,135,-97,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,159,-62,-97,-97,197,199,-63,-97,234,]),'CHECK_END':([67,75,76,77,78,80,81,82,83,84,85,86,107,110,137,139,141,142,143,144,145,146,147,148,149,167,221,],[-97,-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,136,-97,157,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'ADD_END':([75,76,77,78,80,81,82,83,84,85,86,87,114,115,139,140,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,139,-69,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'MUL_END':([75,76,77,78,80,81,82,83,84,85,86,88,115,116,139,140,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,-69,141,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'SUB_END':([75,76,77,78,80,81,82,83,84,85,86,89,115,117,139,140,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,-69,142,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'DIV_END':([75,76,77,78,80,81,82,83,84,85,86,90,115,118,139,140,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,-69,143,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'OR_END':([75,76,77,78,80,81,82,83,84,85,86,91,115,119,139,140,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,-69,144,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'AND_END':([75,76,77,78,80,81,82,83,84,85,86,92,115,120,139,140,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,-69,145,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'MAX_END':([75,76,77,78,80,81,82,83,84,85,86,93,115,121,139,140,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,-69,146,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'MIN_END':([75,76,77,78,80,81,82,83,84,85,86,94,115,122,139,140,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,-69,147,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'EQ_END':([75,76,77,78,80,81,82,83,84,85,86,95,115,123,139,140,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,-69,148,-81,-68,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'NOT_END':([75,76,77,78,80,81,82,83,84,85,86,96,124,139,141,142,143,144,145,146,147,148,149,167,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-97,149,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-63,]),'INDEX_END':([75,76,77,78,80,81,82,83,84,85,86,139,141,142,143,144,145,146,147,148,149,167,193,204,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-97,213,-63,]),'DIMENSION_END':([75,76,77,78,80,81,82,83,84,85,86,139,141,142,143,144,145,146,147,148,149,167,196,207,221,],[-70,-71,-72,-64,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-62,-97,216,-63,]),'TO_END':([102,155,163,164,167,177,221,],[-64,-97,176,-61,-62,-60,-63,]),'LBRACKET':([103,159,161,197,199,202,205,228,231,242,243,],[130,169,171,208,210,212,214,233,235,244,245,]),'DIMENSIONS_START':([103,161,162,],[132,173,175,]),'COUNT':([132,173,175,],[152,185,187,]),'TO_START':([135,],[155,]),'DO_START':([136,157,],[156,166,]),'DIM_START':([168,],[180,]),'ASSIGN_END':([176,],[188,]),'WHILE_END':([178,],[189,]),'INDEX_START':([180,191,192,203,213,],[193,193,-66,-65,-67,]),'DIMENSION_START':([182,194,195,206,216,218,220,226,227,],[196,196,-54,-53,-55,196,196,196,196,]),'CONDITION_END':([190,],[201,]),'DIM_END':([191,192,203,213,],[202,-66,-65,-67,]),'DIMENSIONS_END':([194,195,206,216,226,227,],[205,-54,-53,-55,231,232,]),'VALUES_START':([205,231,232,],[215,236,237,]),'VALUES_END':([223,224,229,234,240,241,],[228,-51,-50,-52,242,243,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'blocks':([2,],[3,]),'block':([2,3,],[4,12,]),'vardeclaration':([2,3,35,38,156,165,166,179,],[5,5,40,40,40,40,40,40,]),'function':([2,3,],[6,6,]),'empty':([2,3,9,13,35,38,50,52,53,54,55,56,57,66,67,68,87,88,89,90,91,92,93,94,95,96,110,114,116,117,118,119,120,121,122,123,131,155,156,163,165,166,172,174,179,193,196,225,],[7,7,21,21,46,46,71,78,78,78,78,78,102,78,78,71,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,102,46,102,46,46,78,78,46,78,78,78,]),'declarations':([9,],[13,]),'declaration':([9,13,],[14,25,]),'declaration_var':([9,13,],[15,15,]),'declaration_var_init':([9,13,],[16,16,]),'declaration_var_const':([9,13,],[17,17,]),'declaration_array':([9,13,],[18,18,]),'declaration_array_init':([9,13,],[19,19,]),'declaration_array_const':([9,13,],[20,20,]),'id':([26,138,],[28,158,]),'funcname':([27,51,],[30,73,]),'statements':([35,156,166,],[38,165,179,]),'statement':([35,38,156,165,166,179,],[39,65,39,65,39,65,]),'assignment':([35,38,156,165,166,179,],[41,41,41,41,41,41,]),'while':([35,38,156,165,166,179,],[42,42,42,42,42,42,]),'switch':([35,38,156,165,166,179,],[43,43,43,43,43,43,]),'call':([35,38,156,165,166,179,],[44,44,44,44,44,44,]),'operator':([35,38,156,165,166,179,],[45,45,45,45,45,45,]),'type':([36,133,134,],[58,153,154,]),'conditions':([50,],[68,]),'condition':([50,68,],[69,109,]),'expression':([52,53,54,55,56,66,67,87,88,89,90,91,92,93,94,95,96,110,114,116,117,118,119,120,121,122,123,131,172,174,193,196,225,],[74,97,98,99,100,106,107,115,115,115,115,115,115,115,115,115,124,137,140,140,140,140,140,140,140,140,140,151,184,186,204,207,230,]),'variable':([52,53,54,55,56,57,66,67,87,88,89,90,91,92,93,94,95,96,110,114,116,117,118,119,120,121,122,123,131,155,163,172,174,193,196,225,],[75,75,75,75,75,101,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,164,177,75,75,75,75,75,]),'const':([52,53,54,55,56,66,67,87,88,89,90,91,92,93,94,95,96,110,114,116,117,118,119,120,121,122,123,131,160,172,174,193,196,198,200,225,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,170,76,76,76,76,209,211,76,]),'math':([52,53,54,55,56,66,67,87,88,89,90,91,92,93,94,95,96,110,114,116,117,118,119,120,121,122,123,131,172,174,193,196,225,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'expressions':([87,88,89,90,91,92,93,94,95,],[114,116,117,118,119,120,121,122,123,]),'variables':([155,],[163,]),'indexes':([180,],[191,]),'index':([180,191,],[192,203,]),'dimensions':([182,218,220,],[194,226,227,]),'dimension':([182,194,218,220,226,227,],[195,206,195,195,206,206,]),'values':([215,236,237,],[223,240,241,]),'value':([215,223,236,237,240,241,],[224,229,224,224,229,229,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM_START blocks PROGRAM_END','program',3,'p_program','parser.py',55),
  ('blocks -> blocks block','blocks',2,'p_blocks','parser.py',59),
  ('blocks -> block','blocks',1,'p_blocks','parser.py',60),
  ('block -> vardeclaration','block',1,'p_block','parser.py',67),
  ('block -> function','block',1,'p_block','parser.py',68),
  ('block -> empty','block',1,'p_block','parser.py',69),
  ('block -> error','block',1,'p_block_error','parser.py',73),
  ('function -> FUNC_START NAME EQUALSIGN funcname RBRACKET statements FUNC_END','function',7,'p_function','parser.py',81),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',85),
  ('statements -> statement','statements',1,'p_statements','parser.py',86),
  ('statement -> vardeclaration','statement',1,'p_statement','parser.py',93),
  ('statement -> assignment','statement',1,'p_statement','parser.py',94),
  ('statement -> while','statement',1,'p_statement','parser.py',95),
  ('statement -> switch','statement',1,'p_statement','parser.py',96),
  ('statement -> call','statement',1,'p_statement','parser.py',97),
  ('statement -> operator','statement',1,'p_statement','parser.py',98),
  ('statement -> empty','statement',1,'p_statement','parser.py',99),
  ('statement -> error','statement',1,'p_statement_error','parser.py',103),
  ('assignment -> ASSIGN_START VALUE_START expression VALUE_END TO_START variables TO_END ASSIGN_END','assignment',8,'p_assignment','parser.py',111),
  ('while -> WHILE_START CHECK_START expression CHECK_END DO_START statements DO_END WHILE_END','while',8,'p_while','parser.py',115),
  ('switch -> SWITCH_START conditions SWITCH_END','switch',3,'p_switch','parser.py',119),
  ('conditions -> conditions condition','conditions',2,'p_conditions','parser.py',123),
  ('conditions -> condition','conditions',1,'p_conditions','parser.py',124),
  ('condition -> CONDITION_START CHECK_START expression CHECK_END DO_START statements DO_END CONDITION_END','condition',8,'p_condition','parser.py',131),
  ('condition -> empty','condition',1,'p_condition','parser.py',132),
  ('condition -> error','condition',1,'p_condition_error','parser.py',139),
  ('call -> CALL_START funcname CALL_END','call',3,'p_call','parser.py',147),
  ('funcname -> ID','funcname',1,'p_funcname','parser.py',151),
  ('funcname -> MAIN','funcname',1,'p_funcname','parser.py',152),
  ('vardeclaration -> VARDECLARATION_START declarations VARDECLARATION_END','vardeclaration',3,'p_vardeclaration','parser.py',156),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','parser.py',160),
  ('declarations -> declaration','declarations',1,'p_declarations','parser.py',161),
  ('declaration -> declaration_var','declaration',1,'p_declaration','parser.py',168),
  ('declaration -> declaration_var_init','declaration',1,'p_declaration','parser.py',169),
  ('declaration -> declaration_var_const','declaration',1,'p_declaration','parser.py',170),
  ('declaration -> declaration_array','declaration',1,'p_declaration','parser.py',171),
  ('declaration -> declaration_array_init','declaration',1,'p_declaration','parser.py',172),
  ('declaration -> declaration_array_const','declaration',1,'p_declaration','parser.py',173),
  ('declaration -> empty','declaration',1,'p_declaration','parser.py',174),
  ('declaration_var -> VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END LBRACKET VAR_END','declaration_var',9,'p_declaration_var','parser.py',178),
  ('declaration_var -> VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END LBRACKET VAR_END','declaration_var',12,'p_declaration_var','parser.py',179),
  ('declaration_var_const -> VAR_START EQUALSIGN id CONST EQUALSIGN TRUE RBRACKET TYPE_START type TYPE_END VALUE_START expression VALUE_END LBRACKET VAR_END','declaration_var_const',15,'p_declaration_var_const','parser.py',183),
  ('declaration_var_init -> VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END VALUE_START expression VALUE_END LBRACKET VAR_END','declaration_var_init',12,'p_declaration_var_init','parser.py',187),
  ('declaration_var_init -> VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END VALUE_START expression VALUE_END LBRACKET VAR_END','declaration_var_init',15,'p_declaration_var_init','parser.py',188),
  ('declaration_array -> VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END LBRACKET VAR_END','declaration_array',16,'p_declaration_array','parser.py',192),
  ('declaration_array -> VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END LBRACKET VAR_END','declaration_array',19,'p_declaration_array','parser.py',193),
  ('declaration_array_init -> VAR_START EQUALSIGN id RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END VALUES_START values VALUES_END LBRACKET VAR_END','declaration_array_init',19,'p_declaration_array_init','parser.py',197),
  ('declaration_array_init -> VAR_START EQUALSIGN id CONST EQUALSIGN FALSE RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END VALUES_START values VALUES_END LBRACKET VAR_END','declaration_array_init',22,'p_declaration_array_init','parser.py',198),
  ('declaration_array_const -> VAR_START EQUALSIGN id CONST EQUALSIGN TRUE RBRACKET TYPE_START type TYPE_END DIMENSIONS_START COUNT EQUALSIGN const RBRACKET dimensions DIMENSIONS_END VALUES_START values VALUES_END LBRACKET VAR_END','declaration_array_const',22,'p_declaration_array_const','parser.py',202),
  ('values -> values value','values',2,'p_values','parser.py',206),
  ('values -> value','values',1,'p_values','parser.py',207),
  ('value -> VALUE_START expression VALUE_END','value',3,'p_value','parser.py',214),
  ('dimensions -> dimensions dimension','dimensions',2,'p_dimensions','parser.py',218),
  ('dimensions -> dimension','dimensions',1,'p_dimensions','parser.py',219),
  ('dimension -> DIMENSION_START expression DIMENSION_END','dimension',3,'p_dimension','parser.py',226),
  ('type -> INT','type',1,'p_type','parser.py',230),
  ('type -> CELL','type',1,'p_type','parser.py',231),
  ('type -> BOOL','type',1,'p_type','parser.py',232),
  ('id -> ID','id',1,'p_id','parser.py',236),
  ('variables -> variables variable','variables',2,'p_variables','parser.py',240),
  ('variables -> variable','variables',1,'p_variables','parser.py',241),
  ('variable -> VAR_START NAME EQUALSIGN id VAR_END','variable',5,'p_variable','parser.py',248),
  ('variable -> VAR_START NAME EQUALSIGN id RBRACKET DIM_START indexes DIM_END LBRACKET VAR_END','variable',10,'p_variable','parser.py',249),
  ('variable -> empty','variable',1,'p_variable','parser.py',250),
  ('indexes -> indexes index','indexes',2,'p_indexes','parser.py',259),
  ('indexes -> index','indexes',1,'p_indexes','parser.py',260),
  ('index -> INDEX_START expression INDEX_END','index',3,'p_index','parser.py',267),
  ('expressions -> expressions expression','expressions',2,'p_expressions','parser.py',271),
  ('expressions -> expression','expressions',1,'p_expressions','parser.py',272),
  ('expression -> variable','expression',1,'p_expression','parser.py',279),
  ('expression -> const','expression',1,'p_expression','parser.py',280),
  ('expression -> math','expression',1,'p_expression','parser.py',281),
  ('expression -> empty','expression',1,'p_expression','parser.py',282),
  ('const -> TRUE','const',1,'p_const','parser.py',286),
  ('const -> FALSE','const',1,'p_const','parser.py',287),
  ('const -> NUMBER','const',1,'p_const','parser.py',288),
  ('const -> EMPTY','const',1,'p_const','parser.py',289),
  ('const -> WALL','const',1,'p_const','parser.py',290),
  ('const -> EXIT','const',1,'p_const','parser.py',291),
  ('const -> UNDEF','const',1,'p_const','parser.py',292),
  ('math -> ADD_START expressions ADD_END','math',3,'p_math','parser.py',296),
  ('math -> MUL_START expressions MUL_END','math',3,'p_math','parser.py',297),
  ('math -> SUB_START expressions SUB_END','math',3,'p_math','parser.py',298),
  ('math -> DIV_START expressions DIV_END','math',3,'p_math','parser.py',299),
  ('math -> OR_START expressions OR_END','math',3,'p_math','parser.py',300),
  ('math -> AND_START expressions AND_END','math',3,'p_math','parser.py',301),
  ('math -> MAX_START expressions MAX_END','math',3,'p_math','parser.py',302),
  ('math -> MIN_START expressions MIN_END','math',3,'p_math','parser.py',303),
  ('math -> EQ_START expressions EQ_END','math',3,'p_math','parser.py',304),
  ('math -> NOT_START expression NOT_END','math',3,'p_math','parser.py',305),
  ('operator -> LEFT_START expression LEFT_END','operator',3,'p_operator','parser.py',309),
  ('operator -> RIGHT_START expression RIGHT_END','operator',3,'p_operator','parser.py',310),
  ('operator -> UP_START expression UP_END','operator',3,'p_operator','parser.py',311),
  ('operator -> DOWN_START expression DOWN_END','operator',3,'p_operator','parser.py',312),
  ('operator -> SENDDRONS_START expression SENDDRONS_END','operator',3,'p_operator','parser.py',313),
  ('operator -> GETDRONSCOUNT_START variable GETDRONSCOUNT_END','operator',3,'p_operator','parser.py',314),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',322),
]
