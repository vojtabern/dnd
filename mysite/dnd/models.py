from django.db import models


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

def uploadnuto(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.region.nazev, instance.nazev, instance.changed_filename, filename)

def upload_mapa(instance, filename):
    return '{0}/{1}/{2}'.format(instance.nazev, instance.changed_filename, filename)
def upload_vladce(instance, filename):
    lowercase_text = instance.jmeno.lower()
    converted_text = lowercase_text.replace(' ', '_')
    return '{0}/{1}/{2}/{3}.jpg'.format(instance.stat_nazev.region.nazev, instance.stat_nazev.nazev, instance.changed_filename, converted_text)


def upload_mesto(instance, filename):
    if instance.hlavni == "ne":
        return '{0}/{1}/{2}/{3}.jpg'.format(instance.stat_nazev.region.nazev, instance.stat_nazev.nazev, instance.changed_filename, instance.nazev)
    else:
        return '{0}/{1}/capital/{2}.jpg'.format(instance.stat_nazev.region.nazev, instance.stat_nazev.nazev, instance.nazev)


def get_npc_upload_path(instance, filename):
    mesto_names = "_".join([mesto.stat_nazev.region.nazev + "/" + mesto.stat_nazev.nazev for mesto in instance.mesto.all()])
    return f"{mesto_names}/NPCs/{instance.vztahHraci}/{instance.jmeno}_{instance.prijmeni}.jpg"


class Opevneni(models.Model):
    typ = models.CharField(max_length=45, primary_key=True, verbose_name='Typ opevnění')

    class Meta:
        ordering = ["typ"]
        verbose_name = 'Opevnění'
        verbose_name_plural = 'Opevnění'

    def __str__(self):
        return self.typ


class Povaha(models.Model):
    povaha = models.CharField(max_length=45, primary_key=True, verbose_name="Typ povahy")

    class Meta:
        ordering = ["povaha"]
        verbose_name = 'Povaha'
        verbose_name_plural = 'Povahy'

    def __str__(self):
        return self.povaha


class Region(models.Model):
    nazev = models.CharField(max_length=50, primary_key=True, verbose_name='Jméno regionu')
    podnebi = models.CharField(max_length=50, choices=[
        ('tropicke', 'tropicke'),
        ('subtropicke', 'subtropicke'),
        ('mírné', 'mírné'),
        ('subpolární', 'subpolární'),
        ('polární', 'polární'),
    ], verbose_name='Podnebí')
    popis = models.TextField(blank=True, verbose_name='Popis', help_text="Popište základní geografické části regionu, jeho historii a státy které se zde nachází")
    changed_filename = models.CharField(max_length=50, default="mapa", editable=False)
    mapa = models.ImageField(upload_to=upload_mapa, blank=True, verbose_name="Mapa")
    class Meta:
        ordering = ["nazev"]
        verbose_name = 'Region'
        verbose_name_plural = 'Regiony'

    def __str__(self):
        return f"{self.nazev} ({self.podnebi})"


class PolitickeUsporadani(models.Model):
    nazev = models.CharField(max_length=45, primary_key=True, verbose_name="Název")
    popis = models.CharField(max_length=45, blank=True, verbose_name="Popis", help_text="Popis jak daný systém funguje")

    class Meta:
        ordering = ["nazev"]
        verbose_name = 'Politické uspořádání'
        verbose_name_plural = 'Politická uspořádání'

    def __str__(self):
        return self.nazev


class Stat(models.Model):
    nazev = models.CharField(max_length=50, primary_key=True)
    rozloha = models.CharField(max_length=50, choices=[
        ('obrovská', 'obrovská'),
        ('velka', 'velka'),
        ('stredni', 'stredni'),
        ('mala', 'mala'),
    ])
    politicke_usporadani = models.OneToOneField(PolitickeUsporadani, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    changed_filename = models.CharField(max_length=50,default="vlajka", editable=False)
    vlajka = models.ImageField(upload_to=uploadnuto, blank=True, verbose_name="Vlajka")

    class Meta:
        ordering = ["nazev"]
        verbose_name = 'Stát'
        verbose_name_plural = 'Státy'

    def __str__(self):
        return self.nazev


class TypMesta(models.Model):
    typ = models.CharField(max_length=50, primary_key=True, verbose_name="Typ města" ,help_text="Přístav, vesnice, město etc.")

    class Meta:
        ordering = ["typ"]
        verbose_name = 'Typ města'
        verbose_name_plural = 'Typy města'

    def __str__(self):
        return f"{self.typ}"


class Mesto(models.Model):
    nazev = models.CharField(max_length=50, primary_key=True, verbose_name="Název města")
    pocet_obyvatel = models.IntegerField(verbose_name="Počet obyvatel města")
    changed_filename = models.CharField(max_length=50, default="mesto_vesnice", editable=False)
    mapa = models.ImageField(upload_to=upload_mesto, blank=True)
    hlavni = models.CharField(max_length=20, choices=[
        ('ano','Ano'),
        ('ne','Ne'),
    ], verbose_name="Jedná se o hlavní město?")
    stat_nazev = models.ForeignKey(Stat, on_delete=models.CASCADE, verbose_name="Stát")
    typ_mesta = models.ForeignKey(TypMesta, on_delete=models.CASCADE, verbose_name="Typ města")

    opevneni_typ = models.ManyToManyField(Opevneni,verbose_name="Typ opevnění")

    class Meta:
        ordering = ["nazev"]
        verbose_name = 'Město'
        verbose_name_plural = 'Města'

    def __str__(self):
        if self.hlavni=='ne':
            return f"{self.stat_nazev} {self.typ_mesta}: {self.nazev}"
        else:
            return f"{self.stat_nazev} Hlavní město je {self.typ_mesta}: {self.nazev})"


class NPC(models.Model):
    idnpc = models.IntegerField(primary_key=True)
    jmeno = models.CharField(max_length=45, null=True)
    prijmeni = models.CharField(max_length=45)
    rasa = models.CharField(max_length=45, choices=[
        ('elf', 'Elf'),
        ('trpaslík', 'Trpaslík'),
        ('člověk', 'Člověk'),
        ('gnóm', 'Gnóm'),
        ('půlork', 'Půlork'),
        ('drakorozený', 'Drakorozený'),
        ('zvíře', 'zvíře'),
        ('půlčík', 'Půlčík'),
        ('půlelf', 'Půl-elf'),
        ('tiefling', 'Tiefling'),
        ('jine', 'Jiné'),
    ])
    vek = models.IntegerField(default=20, verbose_name="Věk")
    vyska = models.IntegerField(blank=True, verbose_name="Výška")
    oci = models.CharField(max_length=45, blank=True, verbose_name="Oči")
    oblicej = models.CharField(max_length=45, blank=True, verbose_name="Obličej")
    kladne_vlastnosti = models.CharField(max_length=150, blank=True, verbose_name="Kladné vlastnosti")
    zaporne_vlastnosti = models.CharField(max_length=150, blank=True, verbose_name="Záporné vlastnosti")
    specifickeZnaky = models.CharField(max_length=45, blank=True, verbose_name="Specifické znaky",
                                          help_text="Tetování etc.")
    #změnit (enum)
    vztahHraci = models.CharField(max_length=150, blank=True,  verbose_name="Vztah k hráčům", choices=[
        ('friendly','Přátelský'),
        ('neutrall', 'Neutrální'),
        ('hostile', 'Nepřátelský'),
    ])

    stat_nazev = models.ForeignKey(Stat, on_delete=models.CASCADE, verbose_name="Stát")
    povaha = models.ForeignKey(Povaha, on_delete=models.CASCADE, verbose_name="Povaha")
    fotka = models.ImageField(upload_to=get_npc_upload_path, verbose_name="Fotka", blank=True)
    mesto = models.ManyToManyField(Mesto)

    class Meta:
        ordering = ["prijmeni"]
        verbose_name = 'NPC'
        verbose_name_plural = 'NPCs'

    def __str__(self):
        return f"NPC: {self.jmeno} {self.prijmeni} ({self.rasa} : {self.povaha})"


class Spravce(models.Model):
    spravce = models.ForeignKey(NPC, on_delete=models.CASCADE, verbose_name="Správce města")
    mesto = models.ForeignKey(Mesto, on_delete=models.CASCADE, verbose_name="Město")

    class Meta:
        ordering = ["spravce"]
        verbose_name = 'Správce města'
        verbose_name_plural = 'Správci měst'

    def __str__(self):
        return f"{self.mesto.nazev} {self.spravce.prijmeni}"


class VladceStatu(models.Model):
    vladce = models.ForeignKey(NPC, on_delete=models.CASCADE, verbose_name="Vládce státu")
    stat = models.ForeignKey(Stat, on_delete=models.CASCADE, verbose_name="Stát")

    class Meta:
        ordering = ["vladce"]
        verbose_name = 'Vládce Státu'
        verbose_name_plural = 'Vládci Států'

    def __str__(self):
        return f"{self.stat.nazev} {self.vladce.prijmeni}"


class Budova(models.Model):
    nazev = models.CharField(max_length=50, primary_key=True)
    typ_budovy = models.CharField(max_length=50, choices=[
        ('inn', 'Hospoda (inn)'),
        ('church', 'Kostel (church)'),
        ('market', 'Tržiště (market)'),
        ('guild', 'Cech (guild)'),
        ('temple', 'Chrám (temple)'),
        ('library', 'Knihovna (library)'),
        ('castle', 'Hrad (castle)'),
        ('blacksmith', 'Kovárna (blacksmith)'),
        ('shop', 'Obchod (shop)'),
        ('magic_shop', 'Obchod s magickými předměty (magic shop)'),
    ], verbose_name="Typ budovy")
    mesto_nazev = models.ForeignKey(Mesto, on_delete=models.CASCADE, verbose_name="Město")
    vlastnik = models.ForeignKey(NPC, on_delete=models.CASCADE)

    class Meta:
        ordering = ["nazev"]
        verbose_name = 'Budova'
        verbose_name_plural = 'Budovy'

    def __str__(self):
        return f"Budova: {self.nazev} : {self.vlastnik.prijmeni}"
# Create your models here.


class StatTable(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE, verbose_name="NPC")
    sila = models.IntegerField(
        default=10,
        verbose_name="Síla",
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    obratnost = models.IntegerField(
        default=10,
        verbose_name="Obratnost",
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    vydrz = models.IntegerField(
        default=10,
        verbose_name="Výdrž",
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    inteligence = models.IntegerField(
        default=10,
        verbose_name="Inteligence",
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    moudrost = models.IntegerField(
        default=10,
        verbose_name="Inteligence",
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    charisma = models.IntegerField(
        default=10,
        verbose_name="Charisma",
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    sila_modifier = models.IntegerField(editable=False)
    obratnost_modifier = models.IntegerField(editable=False)
    vydrz_modifier = models.IntegerField(editable=False)
    inteligence_modifier = models.IntegerField(editable=False)
    moudrost_modifier = models.IntegerField(editable=False)
    charisma_modifier = models.IntegerField(editable=False)

    def save(self, *args, **kwargs):
        self.sila_modifier = (self.sila - 10) // 2
        self.obratnost_modifier = (self.obratnost - 10) // 2
        self.inteligence_modifier = (self.inteligence - 10) // 2
        self.charisma_modifier = (self.charisma - 10) // 2
        self.vydrz_modifier = (self.vydrz - 10) // 2
        self.moudrost_modifier = (self.moudrost - 10) // 2
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["npc"]
        verbose_name = 'Schopnosti'
        verbose_name_plural = 'Schopnosti'

    def __str__(self):
        return f"NPC: {self.npc.prijmeni} : s[{self.sila_modifier}] o[{self.obratnost_modifier}] v[{self.vydrz_modifier}] " \
               f"i[{self.inteligence_modifier}] m[{self.moudrost_modifier}] ch[{self.charisma_modifier}]"