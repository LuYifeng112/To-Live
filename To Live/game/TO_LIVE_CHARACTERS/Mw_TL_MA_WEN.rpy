python:

    import TL_defines_character
init 10:
  default Mw = Char( 
      mood ="Neutral",
      bond = 0,
      pol = None,
      rel = GetMax(MwBelief),
      traits = MaWen_traits,
      skillset = MaWenSkills,
      convolog = MaWenConvo,
      eventlog = MaWenLog
      )
define MaWen_traits = [
  __("Bitter"), 
  __("Frustrated"),
  __("Patient"),
  __("Rational"),
  __("Rebellious"),
  __("Religious"),
  __("Self-Controlled"),
  __("Self-Hating"),
  __("Self-Righteous"),
  __("Short-Tempered"),
  __("Suppressed")
  ]
define MaWenSkills = dict(

  )
define MaWenConvo = [
  ]
define MaWenLog = set(
  )
default MwPol = {
    'Fascism':0,
    'Communism':-2,
    'Centrism':4,
    'Anarchism':2,
    'Conservatism':0,
    'Corporatism':0,
    'Liberalism':0,
    'Libertarianism':0,
    'Moralism':0,
    'Nationalism':1,
    'Progressivism':0
}
default MwBelief = {
    'Atheism':2,
    'Buddhism':3,
    'Christianity':1,
    'Communism':-2,
    'Islam':-1,
    'Shintoism':-2,
    'Taoism':1,
    'Yiguandao':0
}
default MW_impression = None