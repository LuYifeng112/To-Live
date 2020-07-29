python:

    import TL_defines_character

default Mw = Char( 
    mood ="Neutral",
    bond = 0,
    pol = None,
    rel = "Buddhism",
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
default MW_impression = None