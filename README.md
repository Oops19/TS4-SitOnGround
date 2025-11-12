# 🪑 Sit On Ground

### ~~Sit Here~~
### Kneel Here 
### Sit Cross Legged Here

This mod lets Sims sit down.
It’s my first shameless copy-and-paste mod using EA XML code with only a few lines edited.

Originally, it was meant to support three sit interactions, but I never got the first one ("Sit Here") working.  
When testing the animation with Pose Player, it looked odd for teen+ Sims — so maybe it's better that it's not included.

The mod offers:

- **Kneel Here** — similar to the `MizoreYukii_KneelAnywhere` mod.  
  If you see two "Kneel Here" interactions, now you know why.  
  This version includes references to infants, which didn’t exist when MizoreYukii created their mod.

- **Sit Cross Legged Here** — lets Sims sit cross-legged on the ground.  
  *(Vanilla feature: To sit like this on a bed, click the pillow and choose "Sit")*

This mod doesn’t override any default tuning, so it’s less likely to break after updates — though copying content can still lead to missing data if EA changes things.

## 🔄 Updates

Don’t expect frequent updates — I hope it works for a long time.

One day I might extend [Patch-XML](https://github.com/Oops19/TS4-PatchXML) to read the tunings I used, patch them, and add them to TS4 dynamically.

## 🧑‍💻 Development

Skip this section if you just want to use the mod.

I studied MizoreYukii’s mod and used the S4S tuning browser to figure out which interaction to clone.  
Once the first interaction is selected, you’ll find references to other interactions, affordances, and ASMs.  
Cloning the rest is fairly straightforward.

If things don’t work as expected, check the vanilla logs.

It’s important to define your naming conventions early — otherwise you’ll end up with a mess.  
I did this for the tunings, but not for the ASM and postures I cloned later.

## 🔢 FNV Values:
### STBL
* Source: 'Sit Here'
* Clone2: 'Kneel Here' -> 56B3B3D2 0x56B3B3D2  # Also prepend 0x here as we need to paste it later.
* Clone3: 'Sit Cross Legged Here' -> 0xD4301D29
* ==> Add this to a new STBL and then copy this STBL to all languages (with S4S).

### Sources and 3x Clones:
* n="terrain-gohere_AndSitOnGround" s="156620">
* n="o19:terrain-gohere_AndSitOnGround_Normal" s="8633370080534645170"><!-- 77CFE458C0C0C9B2 -->
* n="o19:terrain-gohere_AndSitOnGround_Kneel" s="2269303342278328074"><!-- 1F7E2F5DD41B3F0A -->
* n="o19:terrain-gohere_AndSitOnGround_CrossLegged" s="4082710649035378841"><!-- 38A8B3B444755099 -->


* n="sitOnGround" s="134348">
* n="o19:sitOnGround_Normal" s="3016438606071826384"><!-- 29DC8AEE31AF87D0 -->
* n="o19:sitOnGround_Kneel" s="9230597816864806592"><!-- 8019ABCF02B916C0 -->
* n="o19:sitOnGround_CrossLegged" s="17292203855871925131"><!-- EFFA3FC9F4E2DB8B -->


* n="terrain-gohere_Together" s="25209">
* n="o19:terrain-gohere_Together_Normal" s="3316269230628814569"><!-- 2E05C14B7F303EE9 -->
* n="o19:terrain-gohere_Together_Kneel" s="11410168178282988547"><!-- 9E590F8126060403 -->
* n="o19:terrain-gohere_Together_CrossLegged" s="8007722197060945144"><!-- 6F2124E957D404F8 -->

### Action
Add the 3 Source Tunings to the .package and duplicate them with the HEX values from above.

#### Tuning
##### Source:
```xml
<I c="GoHereSuperInteraction" i="interaction" m="objects.terrain" n="terrain-gohere_AndSitOnGround" s="156620">
<T n="allow_autonomous">False</T>
<T n="display_name">0x7F29DA7B<!--Sit Here--></T>  ############ STBL
<T n="affordance">134348<!--sitOnGround--></T> ################ Source 2
<T n="affordance">25209<!--terrain-gohere_Together--></T> ##### Source 3
<E>TODDLER</E>
</I>
```
    
##### Clone 1:
```xml
<I c="GoHereSuperInteraction" i="interaction" m="objects.terrain" n="o19:terrain-gohere_AndSitOnGround_Normal" s="8633370080534645170"><!-- 77CFE458C0C0C9B2 -->
<T n="allow_autonomous">True</T>
<T n="display_name">0x7F29DA7B<!--Sit Here--></T>
<T n="affordance">3016438606071826384<!-- o19:sitOnGround_Normal --></T>
<T n="affordance">3316269230628814569<!-- o19:terrain-gohere_Together_Normal --></T>
<E>TODDLER</E><E>CHILD</E><E>TEEN</E><E>YOUNGADULT</E><E>ADULT</E><E>ELDER</E>
</I>
```

##### Clone 2:
```xml
<I c="GoHereSuperInteraction" i="interaction" m="objects.terrain" n="o19:terrain-gohere_AndSitOnGround_CrossLegged" s="4082710649035378841"><!-- 38A8B3B444755099 -->
<T n="allow_autonomous">True</T>
<T n="display_name">0x56B3B3D2</T><!-- 'Kneel Here' -->
<T n="affordance">9230597816864806592<!-- o19:sitOnGround_Kneel --></T>
<T n="affordance">11410168178282988547<!-- o19:terrain-gohere_Together_Kneel --></T>
<E>TODDLER</E><E>CHILD</E><E>TEEN</E><E>YOUNGADULT</E><E>ADULT</E><E>ELDER</E>
</I>
```

##### Clone 3:
```xml
<I c="GoHereSuperInteraction" i="interaction" m="objects.terrain" n="o19:terrain-gohere_Together_Kneel" s="11410168178282988547"><!-- 9E590F8126060403 -->
<T n="allow_autonomous">True</T>
<T n="display_name">0xD4301D29</T><!-- Sit Cross Legged Here -->
<T n="affordance">17292203855871925131<!-- o19:sitOnGround_CrossLegged --></T>
<T n="affordance">8007722197060945144<!-- o19:terrain-gohere_Together_CrossLegged --></T>
<E>TODDLER</E><E>CHILD</E><E>TEEN</E><E>YOUNGADULT</E><E>ADULT</E><E>ELDER</E>
</I>
```

#### Tuning
Source 2:
```xml
<I c="SuperInteraction" i="interaction" m="interactions.base.super_interaction" n="sitOnGround" s="134348">
<T n="enabled">134340<!--posture_SitOnGround--></T>
<T n="display_name">0x7F29DA7B<!--Sit Here--></T>
<E>INFANT</E><E>TODDLER</E>
</I>
```

##### Clone 1:
```xml
<I c="SuperInteraction" i="interaction" m="interactions.base.super_interaction" n="o19:sitOnGround_Normal" s="3016438606071826384"><!-- 29DC8AEE31AF87D0 -->
# <T n="enabled">134340<!--posture_SitOnGround--></T>
<T n="enabled">8007608924056666641</T> <!-- o19:posture_SitOnGround -->
<T n="display_name">0x7F29DA7B<!--Sit Here--></T>
<E>CHILD</E><E>TEEN</E><E>YOUNGADULT</E><E>ADULT</E><E>ELDER</E>
</I>
```

##### Clone 2:
```xml
<I c="SuperInteraction" i="interaction" m="interactions.base.super_interaction" n="o19:sitOnGround_Kneel" s="9230597816864806592"><!-- 8019ABCF02B916C0 -->
<T n="enabled">15527<!-- posture_Kneel --></T>
<T n="display_name">0x56B3B3D2</T><!-- 'Kneel Here' -->
<E>CHILD</E><E>TEEN</E><E>YOUNGADULT</E><E>ADULT</E><E>ELDER</E>
</I>
```

##### Clone 3:
```xml
<I c="SuperInteraction" i="interaction" m="interactions.base.super_interaction" n="o19:sitOnGround_CrossLegged" s="17292203855871925131"><!-- EFFA3FC9F4E2DB8B -->
<T n="enabled">283170<!-- posture_CrossLegged --></T>
<T n="display_name">0xD4301D29</T><!-- Sit Cross Legged Here -->
<E>CHILD</E><E>TEEN</E><E>YOUNGADULT</E><E>ADULT</E><E>ELDER</E>
</I>
```

#### Tuning
##### Source 3:
```xml
<I c="GoHereSuperInteraction" i="interaction" m="objects.terrain" n="terrain-gohere_Together" s="25209">
<T n="enabled">15537<!--posture_Stand--></T>
</I>
```

##### Clone 1:
```xml
<I c="GoHereSuperInteraction" i="interaction" m="objects.terrain" n="o19:terrain-gohere_Together_Normal" s="3316269230628814569"><!-- 2E05C14B7F303EE9 -->
<T n="enabled">8007608924056666641</T> <!-- o19:posture_SitOnGround -->
</I>
```

##### Clone 2:
```xml
<I c="GoHereSuperInteraction" i="interaction" m="objects.terrain" n="o19:terrain-gohere_Together_Kneel" s="11410168178282988547"><!-- 9E590F8126060403 -->
<T n="enabled">15527<!--posture_Kneel--></T>
</I>
```

##### Clone 3:
```xml
<I c="GoHereSuperInteraction" i="interaction" m="objects.terrain" n="o19:terrain-gohere_Together_CrossLegged" s="8007722197060945144"><!-- 6F2124E957D404F8 -->
<T n="enabled">283170<!--posture_CrossLegged--></T>
</I>
```

### Part 2
Nothing of the things below is in the .package file as it didn't work.

Part 2 left here for documentation if I ever look again at it.

#### Posture
##### Source:
```xml
<I c="Posture" i="posture" m="postures.posture" n="posture_SitOnGround" s="134340">
  <T n="_asm_key" p="InGame\Sage\SitOnGround_Posture.postureasm">02d5df13:00000000:7974025fad5f6c30</T>
  <T n="factory">134346<!--SitOnGround_Idle_Looping_Basic--></T>
</I>
```

##### Clone:
```xml
<I c="Posture" i="posture" m="postures.posture" n="o19:posture_SitOnGround" s="8007608924056666641"><!-- 6F20BDE3EAA54211 -->
  <T n="_asm_key" p="InGame\Sage\o19_SitOnGround_Posture.postureasm">02d5df13:00000000:233718CB6113A80B</T>
  <T n="factory">2537524176832669707<!--o19:SitOnGround_Idle_Looping_Basic--></T>
</I>
```

#### Animation
##### Source:
```xml
<I c="AnimationElement" i="animation" m="animation.animation_element" n="SitOnGround_Idle_Looping_Basic" s="134346">
  <T n="asm_key" p="InGame\Sage\SitOnGround_Idle.interactionasm">02d5df13:00000000:1bfd81731efec32e</T>
</I>
  ```

##### Clone:
```xml
<I c="AnimationElement" i="animation" m="animation.animation_element" n="o19:SitOnGround_Idle_Looping_Basic" s="2537524176832669707"><!-- 233718CB6113A80B -->
  <T n="asm_key" p="InGame\Sage\o19_SitOnGround_Idle.interactionasm">02d5df13:00000000:A008CADB70EBD9B7</T>
</I>
```

#### ASM (Tools > Game File Cruiser)
##### Source 1:
###### 1BFD81731EFEC32E <ASM name="SitOnGround_Idle" dcc="sage">
```xml
<ParameterSelector parameter="x:age" unique_id="9">
    <Choice value="baby" />
    <Choice value="toddler">
    </Choice>  
</ParameterSelector>
```

##### Clone 1:
###### o19:SitOnGround_Idle -> A008CADB70EBD9B7
    Add child-elder
```xml
    <Choice value="child">
        <Reference target="9" />
    </Choice>
```

##### Source 2:
###### 7974025FAD5F6C30 <ASM name="SitOnGround_Posture" dcc="sage">
```xml
    <ParameterSelector parameter="x:age" unique_id="3">
        <Choice value="baby" />
        <Choice value="toddler">
    </Choice>  
</ParameterSelector>
```

```xml
    <ParameterSelector parameter="x:age" unique_id="8">
        <Choice value="baby" />
        <Choice value="toddler">
    </Choice>  
</ParameterSelector>
```

##### Clone 2:
###### o19:SitOnGround_Posture -> C426D31860D08EB7
Add child-elder:
```xml
    <Choice value="child">
        <Reference target="3" />
    </Choice>
    <Choice value="child">
        <Reference target="8" />
    </Choice>
```




---

# 📝 Addendum

## 🔄 Game compatibility
This mod has been tested with `The Sims 4` 1.119.109, S4CL 3.17, TS4Lib 0.3.42.
It is expected to remain compatible with future releases of TS4, S4CL, and TS4Lib.

## 📦 Dependencies
Download the ZIP file - not the source code.
Required components:
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not already installed, download and install TS4 and the listed mods. All are available for free.

## 📥 Installation
* Locate the localized `The Sims 4` folder (it contains the `Mods` folder).
* Extract the ZIP file directly into this folder.

This will create:
* `Mods/_o19_/$mod_name.ts4script`
* `Mods/_o19_/$mod_name.package`
* `mod_data/$mod_name/*`
* `mod_documentation/$mod_name/*` (optional)
* `mod_sources/$mod_name/*` (optional)

Additional notes:
* CAS and Build/Buy UGC without scripts will create `Mods/o19/$mod_name.package`.
* A log file `mod_logs/$mod_name.txt` will be created once data is logged.
* You may safely delete `mod_documentation/` and `mod_sources/` folders if not needed.

### 📂 Manual Installation
If you prefer not to extract directly into `The Sims 4`, you can extract to a temporary location and copy files manually:
* Copy `mod_data/` contents to `The Sims 4/mod_data/` (usually required).
* `mod_documentation/` is for reference only — not required.
* `mod_sources/` is not needed to run the mod.
* `.ts4script` files can be placed in a folder inside `Mods/`, but storing them in `_o19_` is recommended for clarity.
* `.package` files can be placed in a anywhere inside `Mods/`.

## 🛠️ Troubleshooting
If installed correctly, no troubleshooting should be necessary.
For manual installs, verify the following:
* Does your localized `The Sims 4` folder exist? (e.g. localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...)
  * Does it contain a `Mods/` folder?
    * Does Mods/_o19_/ contain:
      * `ts4lib.ts4script` and `ts4lib.package`?
      * `{mod_name}.ts4script` and/or `{mod_name}.package`
* Does `mod_data/` contain `{mod_name}/` with files?
* Does `mod_logs/` contain:
  * `Sims4CommunityLib_*_Messages.txt`?
  * `TS4-Library_*_Messages.txt`?
  * `{mod_name}_*_Messages.txt`?
* Are there any `last_exception.txt` or `last_exception*.txt` files in `The Sims 4`?


* When installed properly this is not necessary at all.
For manual installations check these things and make sure each question can be answered with 'yes'.
* Does 'The Sims 4' (localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...) exist?
  * Does `The Sims 4` contain the folder `Mods`?
    * Does `Mods` contain the folder `_o19_`? 
      * Does `_19_` contain `ts4lib.ts4script` and `ts4lib.package` files?
      * Does `_19_` contain `{mod_name}.ts4script` and/or `{mod_name}.package` files?
  * Does `The Sims 4` contain the folder `mod_data`?
    * Does `mod_data` contain the folder `{mod_name}`?
      * Does `{mod_name}` contain files or folders?
  * Does `The Sims 4` contain the `mod_logs` ?
    * Does `mod_logs` contain the file `Sims4CommunityLib_*_Messages.txt`?
    * Does `mod_logs` contain the file `TS4-Library_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
    * Does `mod_logs` contain the file `{mod_name}_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
  * Doesn't `The Sims 4` contain the file(s) `last_exception.txt`  and/or `last_exception*.txt` ?
* Share the `The Sims 4/mod_logs/Sims4CommunityLib_*_Messages.txt` and `The Sims 4/mod_logs/{mod_name}_*_Messages.txt`  file.

If issues persist, share:
`mod_logs/Sims4CommunityLib_*_Messages.txt`
`mod_logs/{mod_name}_*_Messages.txt`

## 🕵️ Usage Tracking / Privacy
This mod does not send any data to external servers.
The code is open source, unobfuscated, and fully reviewable.

Note: Some log entries (especially warnings or errors) may include your local username if file paths are involved.
Share such logs with care.

## 🔗 External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## ⚖️ Copyright and License
* © 2020-2025 [Oops19](https://github.com/Oops19)
* `.package` files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* All other content (unless otherwise noted): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 

You may use and adapt this mod and its code — even without owning The Sims 4.
Have fun extending or integrating it into your own mods!

Oops19 / o19 is not affiliated with or endorsed by Electronic Arts or its licensors.
Game content and materials © Electronic Arts Inc. and its licensors.
All trademarks are the property of their respective owners.

## 🧾 Terms of Service
* Do not place this mod behind a paywall.
* Avoid creating mods that break with every TS4 update.
* For simple tuning mods, consider using:
  * [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
  * [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To verify custom tuning structures, use:
  * [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).

## 🗑️ Removing the Mod
Installing this mod creates files in several directories. To fully remove it, delete:
* `The Sims 4/Mods/_o19_/$mod_name.*`
* `The Sims 4/mod_data/_o19_/$mod_name/`
* `The Sims 4/mod_documentation/_o19_/$mod_name/`
* `The Sims 4/mod_sources/_o19_/$mod_name/`

To remove all of my mods, delete the following folders:
* `The Sims 4/Mods/_o19_/`
* `The Sims 4/mod_data/_o19_/`
* `The Sims 4/mod_documentation/_o19_/`
* `The Sims 4/mod_sources/_o19_/`
