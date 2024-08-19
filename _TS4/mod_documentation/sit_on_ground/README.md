# Sit On Ground

### ~~Sit Here~~
### Kneel Here 
### Sit Cross Legged Here

This is a mod to let sims sit down. It's my first shameless copy and paste mod using EA XML code and editing only a few lines.
Actually it should support three sit interactions, but I never got the first one working.
When playing the animation with Pose Player it looked very odd for teen+ sims. So maybe it's better that it isn't included.

So it offers 'Kneel Here' which should be very similar to the 'MizoreYukii_KneelAnywhere' mod. If you end up with two 'Knee Here' interactions you should know why.
Except that it includes references to 'infants' which didn't exist back then when 'MizoreYukii' created this mod.

It also includes 'Sit Cross Legged Here' so sims can sit like this on the ground.
(Vanilla feature: To sit like this on the bed, select the pillow and select 'Sit'.)

I hope that this mod doesn't break as copying content may also lead to missing data after an update.
At least it doesn't replace any default tuning.

This mod requires S4CL to register the interactions.

## Updates
Don't expect updates of this mod, I hope it works quite long.

One day I may extend PatchXML to read the tunings I used, patch them and add them to TS4 dynamically.

# Development
Skip this section if you just want to use the mod.

I looked at MizoreYukiis mod a lot and the S4S tuning browser to figure out which interaction to clone.
After the 1st interaction has been selected one will find references to used interactions, affordances, ASMs in it.
Cloning the other data is quite easy.

If things don't work as expected it makes sense to look at the vanilla logs.

One should as soon as possible define the names one wants to use to avoid ending up with a mess of names.
At least for the tunings I did this, for the ASM and postures which I cloned later I didn't.

## FNV Values:
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





# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.108.349, S4CL 3.7, TS4Lib 0.3.24 (2024-07-25).
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2024 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
