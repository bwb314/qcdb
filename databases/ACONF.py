"""
| Database of <description of members and reference energy type>.
| Geometries from <Reference>.
http://www.thch.uni-bonn.de/tc/downloads/GMTKN/GMTKN30/ACONF.html
| Reference interaction energies from <Reference>.
Taken from Gruzman, D.; Karton, A.; Martin J. M. L. J. Phys. Chem. A 2009, 113, 11974-11983.
(W1hval reference values); all values are in kcal/mol.


- **benchmark**

  - ``'<benchmark_name>'`` <Reference>.
  - |dl| ``'<default_benchmark_name>'`` |dr| <Reference>.

- **subset**

  - ``'small'`` <members_description>
  - ``'large'`` <members_description>
  - ``'<subset>'`` <members_description>

"""
import re
import qcdb

# <<< ACONF Database Module >>>
dbse = 'ACONF'

# <<< Database Members >>>
HRXN = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', ]

# <<< Chemical Systems Involved >>>
RXNM = {}     # reaction matrix of reagent contributions per reaction
ACTV = {}     # order of active reagents per reaction
ACTV['%s-%s'            % (dbse, '1'                     )] = ['%s-%s-reagent'      % (dbse, 'B_T'),
                                                               '%s-%s-reagent'      % (dbse, 'B_G') ]
RXNM['%s-%s'            % (dbse, '1'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '1')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '2'                     )] = ['%s-%s-reagent'      % (dbse, 'P_TT'),
                                                               '%s-%s-reagent'      % (dbse, 'P_TG') ]
RXNM['%s-%s'            % (dbse, '2'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '2')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '3'                     )] = ['%s-%s-reagent'      % (dbse, 'P_TT'),
                                                               '%s-%s-reagent'      % (dbse, 'P_GG') ]
RXNM['%s-%s'            % (dbse, '3'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '3')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '4'                     )] = ['%s-%s-reagent'      % (dbse, 'P_TT'),
                                                               '%s-%s-reagent'      % (dbse, 'P_GX') ]
RXNM['%s-%s'            % (dbse, '4'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '4')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '5'                     )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_gtt') ]
RXNM['%s-%s'            % (dbse, '5'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '5')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '6'                     )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_tgt') ]
RXNM['%s-%s'            % (dbse, '6'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '6')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '7'                     )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_tgg') ]
RXNM['%s-%s'            % (dbse, '7'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '7')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '8'                     )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_gtg') ]
RXNM['%s-%s'            % (dbse, '8'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '8')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '9'                     )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_gptpgm') ]
RXNM['%s-%s'            % (dbse, '9'                     )] = dict(zip(ACTV['%s-%s' % (dbse, '9')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '10'                    )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_ggg') ]
RXNM['%s-%s'            % (dbse, '10'                    )] = dict(zip(ACTV['%s-%s' % (dbse, '10')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '11'                    )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_gpxmtp') ]
RXNM['%s-%s'            % (dbse, '11'                    )] = dict(zip(ACTV['%s-%s' % (dbse, '11')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '12'                    )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_tpgpxm') ]
RXNM['%s-%s'            % (dbse, '12'                    )] = dict(zip(ACTV['%s-%s' % (dbse, '12')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '13'                    )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_gpxmgm') ]
RXNM['%s-%s'            % (dbse, '13'                    )] = dict(zip(ACTV['%s-%s' % (dbse, '13')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '14'                    )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_xpgmgm') ]
RXNM['%s-%s'            % (dbse, '14'                    )] = dict(zip(ACTV['%s-%s' % (dbse, '14')], [-1, +1]))

ACTV['%s-%s'            % (dbse, '15'                    )] = ['%s-%s-reagent'      % (dbse, 'H_ttt'),
                                                               '%s-%s-reagent'      % (dbse, 'H_xpgmxp') ]
RXNM['%s-%s'            % (dbse, '15'                    )] = dict(zip(ACTV['%s-%s' % (dbse, '15')], [-1, +1]))

# <<< Reference Values [kcal/mol] >>>
BIND = {}
# Original publication
# Current revision
BIND_ACONF0 = {}
BIND_ACONF0['%s-%s'            % (dbse, '1'                     )] =    0.598
BIND_ACONF0['%s-%s'            % (dbse, '2'                     )] =    0.614
BIND_ACONF0['%s-%s'            % (dbse, '3'                     )] =    0.961
BIND_ACONF0['%s-%s'            % (dbse, '4'                     )] =    2.813
BIND_ACONF0['%s-%s'            % (dbse, '5'                     )] =    0.595
BIND_ACONF0['%s-%s'            % (dbse, '6'                     )] =    0.604
BIND_ACONF0['%s-%s'            % (dbse, '7'                     )] =    0.934
BIND_ACONF0['%s-%s'            % (dbse, '8'                     )] =    1.178
BIND_ACONF0['%s-%s'            % (dbse, '9'                     )] =    1.302
BIND_ACONF0['%s-%s'            % (dbse, '10'                    )] =    1.250
BIND_ACONF0['%s-%s'            % (dbse, '11'                    )] =    2.632
BIND_ACONF0['%s-%s'            % (dbse, '12'                    )] =    2.740
BIND_ACONF0['%s-%s'            % (dbse, '13'                    )] =    3.283
BIND_ACONF0['%s-%s'            % (dbse, '14'                    )] =    3.083
BIND_ACONF0['%s-%s'            % (dbse, '15'                    )] =    4.925
# Set default
BIND = BIND_ACONF0
# Reference information
BINDINFO_ACONF0 = {}
for rxn in HRXN:
    # Table 2
    BINDINFO_ACONF0['%s-%s' % (dbse, rxn)] = {'citation': 'aconf0'}  # W1 ~= CCSD/TQZ + (T)/DTZ

# <<< Comment Lines >>>
TAGL = {}
TAGL['%s-%s'            % (dbse, '1'                     )] = """Butane gauche conformation"""
TAGL['%s-%s'            % (dbse, '2'                     )] = """Pentane trans, gauche conformation"""
TAGL['%s-%s'            % (dbse, '3'                     )] = """Pentane gauche, gauche conformation"""
TAGL['%s-%s'            % (dbse, '4'                     )] = """Pentane gauche, cross conformation"""
TAGL['%s-%s'            % (dbse, '5'                     )] = """Hexane gauche, trans, trans conformation"""
TAGL['%s-%s'            % (dbse, '6'                     )] = """Hexane trans, gauche, trans conformation"""
TAGL['%s-%s'            % (dbse, '7'                     )] = """Hexane trans, gauche, gauche conformation"""
TAGL['%s-%s'            % (dbse, '8'                     )] = """Hexane gauche, trans, gauche conformation"""
TAGL['%s-%s'            % (dbse, '9'                     )] = """Hexane gauche+, trans+, gauche- conformation"""
TAGL['%s-%s'            % (dbse, '10'                    )] = """Hexane gauche, gauche, gauche conformation"""
TAGL['%s-%s'            % (dbse, '11'                    )] = """Hexane gauche+, cross-, trans+ conformation"""
TAGL['%s-%s'            % (dbse, '12'                    )] = """Hexane trans+, gauche+, cross- conformation"""
TAGL['%s-%s'            % (dbse, '13'                    )] = """Hexane gauche+, cross-, gauche- conformation"""
TAGL['%s-%s'            % (dbse, '14'                    )] = """Hexane cross+, gauche-, gauche- conformation"""
TAGL['%s-%s'            % (dbse, '15'                    )] = """Hexane cross+, gauche-, cross+ conformation"""
TAGL['%s-%s-reagent'    % (dbse, 'B_G'                   )] = """Butane gauche"""
TAGL['%s-%s-reagent'    % (dbse, 'B_T'                   )] = """Butane trans"""
TAGL['%s-%s-reagent'    % (dbse, 'H_ggg'                 )] = """Hexane gauche, gauche, gauche"""
TAGL['%s-%s-reagent'    % (dbse, 'H_gptpgm'              )] = """Hexane gauche+, trans+, gauche-"""
TAGL['%s-%s-reagent'    % (dbse, 'H_gpxmgm'              )] = """Hexane gauche+, cross-, gauche-"""
TAGL['%s-%s-reagent'    % (dbse, 'H_gpxmtp'              )] = """Hexane gauche+, cross-, trans+"""
TAGL['%s-%s-reagent'    % (dbse, 'H_gtg'                 )] = """Hexane gauche, trans, gauche"""
TAGL['%s-%s-reagent'    % (dbse, 'H_gtt'                 )] = """Hexane gauche, trans, trans"""
TAGL['%s-%s-reagent'    % (dbse, 'H_tgg'                 )] = """Hexane trans, gauche, gauche"""
TAGL['%s-%s-reagent'    % (dbse, 'H_tgt'                 )] = """Hexane trans, gauche, trans"""
TAGL['%s-%s-reagent'    % (dbse, 'H_tpgpxm'              )] = """Hexane trans+, gauche+, cross-"""
TAGL['%s-%s-reagent'    % (dbse, 'H_ttt'                 )] = """Hexane trans, trans, trans"""
TAGL['%s-%s-reagent'    % (dbse, 'H_xpgmgm'              )] = """Hexane cross+, gauche-, gauche-"""
TAGL['%s-%s-reagent'    % (dbse, 'H_xpgmxp'              )] = """Hexane cross+, gauche-, cross+"""
TAGL['%s-%s-reagent'    % (dbse, 'P_GG'                  )] = """Pentane gauche, gauche"""
TAGL['%s-%s-reagent'    % (dbse, 'P_GX'                  )] = """Pentane gauche, cross"""
TAGL['%s-%s-reagent'    % (dbse, 'P_TG'                  )] = """Pentane trans, gauche"""
TAGL['%s-%s-reagent'    % (dbse, 'P_TT'                  )] = """Pentane trans, trans"""

TAGL['dbse'] = 'comformation energies for alkanes'
TAGL['default'] = 'entire database'

# <<< Geometry Specification Strings >>>
GEOS = {}

GEOS['%s-%s-%s' % (dbse, 'B_G', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                1.115973904000     2.716887402000    -0.967585870143
H               -0.650815962000     3.774459325000    -1.050365317143
H                1.329698134000     1.711163892000    -2.749028672143
H                2.656550341000     4.074139631000    -0.833228242143
C                1.115973904000     0.913769444000     1.278378035857
H                2.873834815000    -0.169625584000     1.296657354857
H                1.087556205000     2.009419345000     3.025172710857
C               -1.115973904000    -0.913769444000     1.278378035857
H               -2.873834815000     0.169625584000     1.296657354857
H               -1.087556205000    -2.009419345000     3.025172710857
C               -1.115973904000    -2.716887402000    -0.967585870143
H                0.650815962000    -3.774459325000    -1.050365317143
H               -2.656550341000    -4.074139631000    -0.833228242143
H               -1.329698134000    -1.711163892000    -2.749028672143
""")

GEOS['%s-%s-%s' % (dbse, 'B_T', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                1.328505717000     3.431071546000     0.000000000000
H                0.356619640000     4.161333478000     1.662323924000
H                0.356619640000     4.161333478000    -1.662323924000
H                3.239625296000     4.193164023000     0.000000000000
C                1.328505717000     0.553062326000     0.000000000000
H                2.349719312000    -0.145403077000    -1.652425539000
H                2.349719312000    -0.145403077000     1.652425539000
C               -1.328505717000    -0.553062326000     0.000000000000
H               -2.349719312000     0.145403077000    -1.652425539000
H               -2.349719312000     0.145403077000     1.652425539000
C               -1.328505717000    -3.431071546000     0.000000000000
H               -0.356619640000    -4.161333478000     1.662323924000
H               -3.239625296000    -4.193164023000     0.000000000000
H               -0.356619640000    -4.161333478000    -1.662323924000
""")

GEOS['%s-%s-%s' % (dbse, 'H_ggg', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C               -1.437310471000     4.141820168000    -0.922722587500
C               -2.495950088000     1.487662220000    -0.562185545500
C               -1.437310471000     0.147933420000     1.764930753500
C                1.437310471000    -0.147933420000     1.764930753500
C                2.495950088000    -1.487662220000    -0.562185545500
C                1.437310471000    -4.141820168000    -0.922722587500
H                0.586364967000     4.106232848000    -1.294779399500
H               -1.743111599000     5.283966777000     0.765254366500
H               -2.343793131000     5.097445152000    -2.503705145500
H               -2.123798790000     0.360157207000    -2.249512433500
H               -4.548069682000     1.592164067000    -0.385467819500
H               -2.320929336000    -1.707970255000     1.938180832500
H               -1.990909479000     1.206348160000     3.450006978500
H                1.990909479000    -1.206348160000     3.450006978500
H                2.320929336000     1.707970255000     1.938180832500
H                4.548069682000    -1.592164067000    -0.385467819500
H                2.123798790000    -0.360157207000    -2.249512433500
H                2.343793131000    -5.097445152000    -2.503705145500
H               -0.586364967000    -4.106232848000    -1.294779399500
H                1.743111599000    -5.283966777000     0.765254366500
""")

GEOS['%s-%s-%s' % (dbse, 'H_gptpgm', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C               -0.923082013000    -0.149222213000     5.120790827000
C                1.351439432000     0.374961321000     3.432390575000
C                1.054457654000    -0.637752286000     0.746024137000
C               -1.054457654000     0.637752286000    -0.746024137000
C               -1.351439432000    -0.374961321000    -3.432390575000
C                0.923082013000     0.149222213000    -5.120790827000
H               -1.337948678000    -2.167168001000     5.173102222000
H               -2.608808304000     0.821552705000     4.453250790000
H               -0.574047733000     0.471823006000     7.051338679000
H                3.029230763000    -0.470035325000     4.283491035000
H                1.701543297000     2.408374517000     3.351034091000
H                0.691214524000    -2.672805764000     0.823109839000
H                2.842404892000    -0.399242410000    -0.252656365000
H               -0.691214524000     2.672805764000    -0.823109839000
H               -2.842404892000     0.399242410000     0.252656365000
H               -3.029230763000     0.470035325000    -4.283491035000
H               -1.701543297000    -2.408374517000    -3.351034091000
H                0.574047733000    -0.471823006000    -7.051338679000
H                2.608808304000    -0.821552705000    -4.453250790000
H                1.337948678000     2.167168001000    -5.173102222000
""")

GEOS['%s-%s-%s' % (dbse, 'H_gpxmgm', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C               -3.735198850450     2.007047739300    -0.089100013200
C               -3.636315158450    -0.866955261700    -0.241746410200
C               -0.986605625450    -1.941553615700    -0.643847975200
C                0.878242122550    -1.283184418700     1.480372223800
C                2.586875671550     0.978356498300     0.912161853800
C                4.605422393550     0.367236121300    -1.050035128200
H               -2.936644110450     2.862175205300    -1.785314283200
H               -2.679664052450     2.714096277300     1.529644938800
H               -5.675034704450     2.668839229300     0.097695620800
H               -4.856532017450    -1.505270686700    -1.777787504200
H               -4.417490088450    -1.668325693700     1.493621092800
H               -0.250872935450    -1.268009918700    -2.452480154200
H               -1.144399634450    -3.989551716700    -0.820367280200
H                2.091621953550    -2.906500618700     1.872743589800
H               -0.187691837450    -0.935087442700     3.215102887800
H                3.508338189550     1.586844488300     2.654521342800
H                1.450428475550     2.569915853300     0.262912474800
H                5.789418873550     2.003253169300    -1.445373364200
H                3.769868708550    -0.241215963700    -2.830056856200
H                5.826232626550    -1.152109244700    -0.382667056200
""")

GEOS['%s-%s-%s' % (dbse, 'H_gpxmtp', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C               -3.451284244150     2.334093828700     0.042495497150
C               -3.843527109150    -0.483389357300    -0.404553201850
C               -1.698844957150    -2.156581095300     0.563704601150
C                0.883488285850    -1.590509895300    -0.626887022850
C                2.549752287850     0.168645477700     0.936209278150
C                5.042085440850     0.756902060700    -0.376598484850
H               -1.815219953150     3.040326005700    -0.986806124850
H               -3.158325693150     2.730257874700     2.043042578150
H               -5.088935905150     3.412959183700    -0.582062722850
H               -4.080886142150    -0.822916426300    -2.427417946850
H               -5.604991727150    -1.072331910300     0.493178138150
H               -2.210310635150    -4.120788745300     0.201075632150
H               -1.555333496150    -1.968156516300     2.617126216150
H                0.608631419850    -0.781128915300    -2.510424160850
H                1.920329913850    -3.352097345300    -0.913089803850
H                2.916491410850    -0.722838427300     2.761646791150
H                1.544658055850     1.920480052700     1.341219132150
H                6.239880700850     1.974170947700     0.771273994150
H                4.713932632850     1.706672674700    -2.174793706850
H                6.088409713850    -0.973769472300    -0.768338682850
""")

GEOS['%s-%s-%s' % (dbse, 'H_gtg', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                0.063836834000     4.749193219000     1.290897902700
C                1.320882563000     3.454874534000    -0.954773096300
C                1.320882563000     0.576627209000    -0.757461136300
C               -1.320882563000    -0.576627209000    -0.757461136300
C               -1.320882563000    -3.454874534000    -0.954773096300
C               -0.063836834000    -4.749193219000     1.290897902700
H                0.945582981000     4.156928527000     3.057058489700
H               -1.938541392000     4.292659986000     1.404939086700
H                0.228755111000     6.796093389000     1.159546827700
H                3.267122698000     4.118007730000    -1.115637911300
H                0.366752351000     4.012755662000    -2.698867353300
H                2.330141750000     0.027246069000     0.957752438700
H                2.384237047000    -0.213729899000    -2.343455248300
H               -2.384237047000     0.213729899000    -2.343455248300
H               -2.330141750000    -0.027246069000     0.957752438700
H               -0.366752351000    -4.012755662000    -2.698867353300
H               -3.267122698000    -4.118007730000    -1.115637911300
H               -0.228755111000    -6.796093389000     1.159546827700
H               -0.945582981000    -4.156928527000     3.057058489700
H                1.938541392000    -4.292659986000     1.404939086700
""")

GEOS['%s-%s-%s' % (dbse, 'H_gtt', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                4.809938082350     1.613958749050    -0.407673705600
C                3.894054035350    -0.892492545950     0.677231213400
C                1.313413987350    -1.700900317950    -0.326821779600
C               -0.831927678650     0.084006352050     0.382857257400
C               -3.407926559650    -0.867096518950    -0.481399475600
C               -5.540884851650     0.934073132050     0.218364168400
H                3.588234009350     3.172871197050     0.147214095400
H                4.845056750350     1.544416833050    -2.467051736600
H                6.712610586350     2.054924419050     0.240105466400
H                3.807332620350    -0.765835551950     2.736303108400
H                5.274094470350    -2.361962373950     0.241828896400
H                0.867501014350    -3.586191120950     0.388819342400
H                1.406205202350    -1.865684423950    -2.385691474600
H               -0.502896148650     1.950498161050    -0.434674110600
H               -0.853512128650     0.340013201050     2.435194169400
H               -3.759228511650    -2.722444613950     0.352385425400
H               -3.373049776650    -1.145551422950    -2.526651804600
H               -7.369916622650     0.228710230050    -0.407110567600
H               -5.248400621650     2.782497271050    -0.641740836600
H               -5.630697858650     1.202189345050     2.258512348400
""")

GEOS['%s-%s-%s' % (dbse, 'H_tgg', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                5.090633162300    -0.860774157250    -0.036019027300
C                2.516924629300    -0.034971458250     0.954255972700
C                0.908064833300     1.186936705750    -1.097268357300
C               -1.604822868700     2.237949388750    -0.142081788300
C               -3.315733537700     0.291066746750     1.130862204700
C               -3.963461686700    -1.937084602250    -0.574658965300
H                6.144531458300     0.750364648750    -0.767724710300
H                4.879084007300    -2.216854756250    -1.572173506300
H                6.225869044300    -1.745243399250     1.434749041700
H                2.760859909300     1.301971885750     2.509729119700
H                1.530782459300    -1.667496292250     1.738983587700
H                0.574310877300    -0.185558053250    -2.603523590300
H                1.986531456300     2.724049274750    -1.957492415300
H               -2.625564031700     3.081494725750    -1.727420165300
H               -1.222270518700     3.770063632750     1.188992065700
H               -5.056654944700     1.229627505750     1.715025641700
H               -2.428365455700    -0.395842982250     2.860870444700
H               -5.316647225700    -3.197363652250     0.327976212700
H               -2.293113986700    -3.047187128250    -1.037074915300
H               -4.790957580700    -1.285148033250    -2.346006850300
""")

GEOS['%s-%s-%s' % (dbse, 'H_tgt', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                1.290418290000     5.543777644000    -0.566643597700
C                1.290418290000     2.670978399000    -0.751513601700
C               -0.057247359000     1.440698749000     1.477180098300
C                0.057247359000    -1.440698749000     1.477180098300
C               -1.290418290000    -2.670978399000    -0.751513601700
C               -1.290418290000    -5.543777644000    -0.566643597700
H                2.238903890000     6.166476373000     1.152249273300
H               -0.636066651000     6.270864837000    -0.514320864700
H                2.248700229000     6.410394645000    -2.168112675700
H                3.233937220000     1.976071350000    -0.828999926700
H                0.393652601000     2.099859741000    -2.517309471700
H               -2.034530024000     2.044949973000     1.491417294300
H                0.779477956000     2.153395678000     3.226053472300
H               -0.779477956000    -2.153395678000     3.226053472300
H                2.034530024000    -2.044949973000     1.491417294300
H               -0.393652601000    -2.099859741000    -2.517309471700
H               -3.233937220000    -1.976071350000    -0.828999926700
H               -2.248700229000    -6.410394645000    -2.168112675700
H               -2.238903890000    -6.166476373000     1.152249273300
H                0.636066651000    -6.270864837000    -0.514320864700
""")

GEOS['%s-%s-%s' % (dbse, 'H_tpgpxm', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                5.124545429850    -0.821571696650     0.230200278100
C                2.291553261850    -0.766731848650    -0.280088099900
C                1.195684152850     1.875573738350     0.050852054100
C               -1.598591308150     2.149886362350    -0.620524126900
C               -3.384234971150     0.481668383350     0.940389541100
C               -4.001670813150    -2.046263426650    -0.301353185900
H                5.531945786850    -0.184913561650     2.146431566100
H                6.125435020850     0.425966820350    -1.067400859900
H                5.901532726850    -2.714701083650     0.015128674100
H                1.344401808850    -2.080739587650     0.995201044100
H                1.913594835850    -1.429770558650    -2.198851619900
H                2.293150080850     3.190486656350    -1.105023414900
H                1.469821032850     2.465478162350     2.013587608100
H               -1.867244204150     1.737587836350    -2.628038627900
H               -2.116555754150     4.129742834350    -0.366270942900
H               -5.152861650150     1.490761275350     1.260786914100
H               -2.559717285150     0.167680961350     2.808037863100
H               -5.256660520150    -3.173023887650     0.879188875100
H               -2.310012672150    -3.155538252650    -0.664855208900
H               -4.944114959150    -1.741579126650    -2.107398330900
""")

GEOS['%s-%s-%s' % (dbse, 'H_ttt', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                2.674302427000     5.422166218000     0.000000000000
C                2.674302427000     2.543888657000     0.000000000000
C                0.016877143000     1.438580366000     0.000000000000
C               -0.016877143000    -1.438580366000     0.000000000000
C               -2.674302427000    -2.543888657000     0.000000000000
C               -2.674302427000    -5.422166218000     0.000000000000
H                1.702484380000     6.152694602000     1.662322034000
H                1.702484380000     6.152694602000    -1.662322034000
H                4.585654442000     6.184115076000     0.000000000000
H                3.696130183000     1.846859446000     1.652501128000
H                3.696130183000     1.846859446000    -1.652501128000
H               -1.009485955000     2.133946619000    -1.654026137000
H               -1.009485955000     2.133946619000     1.654026137000
H                1.009485955000    -2.133946619000     1.654026137000
H                1.009485955000    -2.133946619000    -1.654026137000
H               -3.696130183000    -1.846859446000    -1.652501128000
H               -3.696130183000    -1.846859446000     1.652501128000
H               -4.585654442000    -6.184115076000     0.000000000000
H               -1.702484380000    -6.152694602000     1.662322034000
H               -1.702484380000    -6.152694602000    -1.662322034000
""")

GEOS['%s-%s-%s' % (dbse, 'H_xpgmgm', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                3.287897873900     2.175681783500    -0.184354203300
C                3.225614394900    -0.700244957500    -0.388962395300
C                1.115595486900    -1.967895828500     1.142135176700
C               -1.341760728100    -2.403084606500    -0.316355343300
C               -2.673754879100    -0.036161229500    -1.290699953300
C               -3.537064859100     1.730560606500     0.812850422700
H                3.521052265900     2.749119135500     1.780766184700
H                1.560571154900     3.041699741500    -0.883815491300
H                4.861414123900     2.959987989500    -1.255547270300
H                5.046692308900    -1.423945761500     0.251824790700
H                3.054354196900    -1.259828728500    -2.370043409300
H                0.750687507900    -0.864947805500     2.849294738700
H                1.774042161900    -3.811155346500     1.792100761700
H               -2.656530026100    -3.439126880500     0.895404991700
H               -0.926652178100    -3.642805327500    -1.915537852300
H               -4.317079497100    -0.622531866500    -2.391248024300
H               -1.444025139100     0.971306497500    -2.604102980300
H               -4.574622694100     3.339921179500     0.058356533700
H               -1.947724043100     2.464598211500     1.892991342700
H               -4.778707432100     0.738853193500     2.124941979700
""")

GEOS['%s-%s-%s' % (dbse, 'H_xpgmxp', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C               -0.128949232000     3.311580392000    -2.029579697800
C                1.556287619000     2.621700014000     0.206221262200
C                0.128949232000     1.440114824000     2.434115608200
C               -0.128949232000    -1.440114824000     2.434115608200
C               -1.556287619000    -2.621700014000     0.206221262200
C                0.128949232000    -3.311580392000    -2.029579697800
H               -1.533879248000     4.703439173000    -1.453111225800
H               -1.140649946000     1.683895146000    -2.771248015800
H                0.967390419000     4.127669899000    -3.569473943800
H                2.487363173000     4.344094548000     0.853150057200
H                3.068491710000     1.352769799000    -0.395656465800
H               -1.755980633000     2.283437172000     2.538524859200
H                1.083168261000     1.963139955000     4.187057562200
H               -1.083168261000    -1.963139955000     4.187057562200
H                1.755980633000    -2.283437172000     2.538524859200
H               -3.068491710000    -1.352769799000    -0.395656465800
H               -2.487363173000    -4.344094548000     0.853150057200
H               -0.967390419000    -4.127669899000    -3.569473943800
H                1.533879248000    -4.703439173000    -1.453111225800
H                1.140649946000    -1.683895146000    -2.771248015800
""")

GEOS['%s-%s-%s' % (dbse, 'P_GG', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C               -0.000000000000     3.465207556000    -1.228375028412
C                1.578735674000     1.846481501000     0.554719393588
C                0.000000000000     0.000000000000     2.114327260588
C               -1.578735674000    -1.846481501000     0.554719393588
C                0.000000000000    -3.465207556000    -1.228375028412
H                1.160072550000     4.871687147000    -2.182274693412
H               -3.001909104000    -0.814366077000    -0.523065038412
H               -2.619394549000    -3.072643438000     1.845336104588
H               -1.478540512000     4.461764006000    -0.194921678412
H               -0.912365377000     2.325836955000    -2.679108222412
H               -1.254214919000     1.079311330000     3.350525532588
H                1.254214919000    -1.079311330000     3.350525532588
H                3.001909104000     0.814366077000    -0.523065038412
H                2.619394549000     3.072643438000     1.845336104588
H               -1.160072550000    -4.871687147000    -2.182274693412
H                0.912365377000    -2.325836955000    -2.679108222412
H                1.478540512000    -4.461764006000    -0.194921678412
""")

GEOS['%s-%s-%s' % (dbse, 'P_GX', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C               -3.404458312294     1.325465481941     0.304913513765
C               -2.164476809294    -1.010829217059    -0.843125261235
C                0.077019784706    -2.023884864059     0.692946068765
C                2.657468970706    -1.064151615059    -0.176891025235
C                2.974391136706     1.795963789941    -0.066015132235
H               -4.969436781294     1.989209058941    -0.856313659235
H                2.980649909706    -1.707639219059    -2.112142404235
H                4.117607330706    -1.950937661059     0.979507897765
H               -2.071566541294     2.875543460941     0.516052598765
H               -4.150767798294     0.889989464941     2.174697225765
H                0.101858342706    -4.083281792059     0.590989682765
H               -0.196601200294    -1.548263509059     2.685826531765
H               -3.596828639294    -2.483415202059    -1.011214498235
H               -1.538448383294    -0.602370613059    -2.768674787235
H                4.892650099706     2.342257116941    -0.573716475235
H                1.695878120706     2.748107898941    -1.366534007235
H                2.595060769706     2.508237419941     1.829693730765
""")

GEOS['%s-%s-%s' % (dbse, 'P_TG', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C                4.546836580000    -0.267633332824     0.204358636529
C                1.820224647000    -0.630254742824    -0.644835090471
C                0.069512570000     1.381910374176     0.441969003529
C               -2.652824802000     1.201963106176    -0.493519061471
C               -3.978146331000    -1.228545770824     0.303367050529
H                5.785795741000    -1.715237140824    -0.572435908471
H               -2.670694051000     1.358181085176    -2.552322615471
H               -3.716749983000     2.817183720176     0.222133399529
H                4.687889507000    -0.350751040824     2.257623404529
H                5.262473923000     1.567899096176    -0.396113134471
H                0.830399402000     3.242183095176    -0.033882898471
H                0.090497977000     1.254890552176     2.505738757529
H                1.716901989000    -0.569148562824    -2.706741574471
H                1.172951922000    -2.504158057824    -0.081073135471
H               -5.952887314000    -1.224110583824    -0.275002485471
H               -3.090851948000    -2.886003649824    -0.530895951471
H               -3.921329829000    -1.448368146824     2.351631603529
""")

GEOS['%s-%s-%s' % (dbse, 'P_TT', 'reagent')] = qcdb.Molecule("""
units Bohr
no_com
no_reorient
0 1
C               -0.000000000000     4.786668375000     0.570052852824
C               -0.000000000000     2.403406427000    -1.042905759176
C                0.000000000000     0.000000000000     0.539101030824
C                0.000000000000    -2.403406427000    -1.042905759176
C                0.000000000000    -4.786668375000     0.570052852824
H               -0.000000000000     6.489075277000    -0.585607187176
H                1.652457664000    -2.398523375000    -2.280024327176
H               -1.652457664000    -2.398523375000    -2.280024327176
H                1.662254004000     4.847413617000     1.784604312824
H               -1.662254004000     4.847413617000     1.784604312824
H               -1.653761575000    -0.000000000000     1.779749606824
H                1.653761575000     0.000000000000     1.779749606824
H               -1.652457664000     2.398523375000    -2.280024327176
H                1.652457664000     2.398523375000    -2.280024327176
H                0.000000000000    -6.489075277000    -0.585607187176
H                1.662254004000    -4.847413617000     1.784604312824
H               -1.662254004000    -4.847413617000     1.784604312824
""")

