python:

    import TL_defines_character
init 10:
  default Ts = Char( 
      mood ="Disgruntled",
      bond = 0,
      pol = GetMax(TsPol),
      rel = GetMax(TsRel),
      traits = Tsai_traits,
      skillset = TsaiSkills,
      convolog = TsaiConvo,
      eventlog = TsaiLog
      )
define Tsai_traits = [

  ]
define TsaiSkills = dict(

  )
define TsaiConvo = [
  ]
define TsaiLog = set(
  )
default TsPol = {
    'fascism':0,
    'communism':-7,
    'centrism':-1,
    'anarchism':-3,
    'conservatism':6,
    'corporatism':2,
    'liberalism':0,
    'libertarianism':1,
    'moralism':2,
    'nationalism':4,
    'progressivism':2
}
default TsRel = {
    'atheism':6,
    'buddhism':0,
    'christian':-3,
    'communism':-5,
    'islam':-1,
    'shintoism':-4,
    'taoism':-1,
    'yiguandao':-5
}