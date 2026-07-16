---
title: "AdministrativeRules Structure Reference"
slug: "sdk-for-ios-navigate-structs-administrativerules"
---

# AdministrativeRules

<div class="declaration">

<div class="language">

``` highlight
public struct AdministrativeRules : Hashable
```

</div>

</div>

Represents a set of administrative rules for a country or a state.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11countryCodeAA07CountryE0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-countryCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11countryCodeAA07CountryE0Ovp" class="token"><code>countryCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Country code for which the administrative rules apply.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var countryCode: CountryCode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-countrycode">CountryCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV9stateCodeSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-stateCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV9stateCodeSSSgvp" class="token"><code>stateCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The state code for which the administrative rules apply. It represents the state / province code. It is a 1 to 3 upper-case characters string that follows the ISO 3166-2 standard, but without the preceding country code (e.g. for Texas, the state code will be TX). It will be `nil` if the rules are applying to the entire country and not just a specific state.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var stateCode: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV14adminContextIdAA05AdmineF0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-adminContextId" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV14adminContextIdAA05AdmineF0Vvp" class="token"><code>adminContextId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The administrative context ID used to identify this administrative region. This ID is used internally to load commercial vehicle regulations and other administrative-specific data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var adminContextId: AdminContextId
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-admincontextid">AdminContextId</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV21parentAdminContextIdsSayAA0eF2IdVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-parentAdminContextIds" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV21parentAdminContextIdsSayAA0eF2IdVGvp" class="token"><code>parentAdminContextIds</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of parent administrative context IDs. These represent the administrative hierarchy (e.g., state-\>country). Used internally to load commercial vehicle regulations that may be inherited from parent administrative regions.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var parentAdminContextIds: [AdminContextId]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-admincontextid">AdminContextId</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11drivingSideAA07DrivingE0OSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-drivingSide" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11drivingSideAA07DrivingE0OSgvp" class="token"><code>drivingSide</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The side of the road used for driving in the country or state. Defaults to right driving side.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var drivingSide: DrivingSide?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-drivingside">DrivingSide</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV10unitSystemAA04UnitE0OSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-unitSystem" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV10unitSystemAA04UnitE0OSgvp" class="token"><code>unitSystem</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the measurement system used for distances. Defaults to metric measurement system.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var unitSystem: UnitSystem?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-unitsystem">UnitSystem</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11speedLimitsAA019GeneralVehicleSpeedE0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-speedLimits" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11speedLimitsAA019GeneralVehicleSpeedE0Vvp" class="token"><code>speedLimits</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The general speed limits in the country or state.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedLimits: GeneralVehicleSpeedLimits
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV24timeZoneOffsetsInMinutesSaySdGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-timeZoneOffsetsInMinutes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV24timeZoneOffsetsInMinutesSaySdGvp" class="token"><code>timeZoneOffsetsInMinutes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative (e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes). Defaults to 0 minutes. **Note:** A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of 90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset of -210 minutes. In order to properly calculate the time zone offset, the \[AdministrativeRules.daylight_saving_period\] should be taken into consideration and if the daylight savings time is observed at the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeZoneOffsetsInMinutes: [TimeInterval]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV20daylightSavingPeriodAA8TimeRuleCSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-daylightSavingPeriod" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV20daylightSavingPeriodAA8TimeRuleCSgvp" class="token"><code>daylightSavingPeriod</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Time rule indicating the time periods in which daylight savings applies. If the field is ‘null’ then daylight savings time is not observed in the country or state. **Note:** In order to properly calculate the time zone offset, if the daylight savings time is observed at the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var daylightSavingPeriod: TimeRule?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-timerule">TimeRule</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV17isUturnRestrictedSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isUturnRestricted" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV17isUturnRestrictedSbvp" class="token"><code>isUturnRestricted</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if performing a u-turn maneuver is restricted. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isUturnRestricted: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV22headlightsRequirementsSayAA21HeadlightsRequirementOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-headlightsRequirements" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV22headlightsRequirementsSayAA21HeadlightsRequirementOGvp" class="token"><code>headlightsRequirements</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates in which conditions should the headlights be turned on. Defaults to an empty list, which means that by default there are no special situations in which the headlights should be turned on.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var headlightsRequirements: [HeadlightsRequirement]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-headlightsrequirement">HeadlightsRequirement</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV14isTollRequiredSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isTollRequired" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV14isTollRequiredSbvp" class="token"><code>isTollRequired</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the country or state requires paid fees for usage of the motorways / controlled access roads. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTollRequired: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV21isTollStickerRequiredSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isTollStickerRequired" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV21isTollStickerRequiredSbvp" class="token"><code>isTollStickerRequired</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the country or state requires a toll sticker. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTollStickerRequired: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV20turnOnRedRegulationsSayAA04TurneF10RegulationOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-turnOnRedRegulations" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV20turnOnRedRegulationsSayAA04TurneF10RegulationOGvp" class="token"><code>turnOnRedRegulations</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the regulations for turning on the red color of the traffic light.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var turnOnRedRegulations: [TurnOnRedRegulation]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-turnonredregulation">TurnOnRedRegulation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV22parkingSideRegulationsSayAA07ParkingE10RegulationOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-parkingSideRegulations" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV22parkingSideRegulationsSayAA07ParkingE10RegulationOGvp" class="token"><code>parkingSideRegulations</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the regulations for parking on the side of the road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var parkingSideRegulations: [ParkingSideRegulation]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-parkingsideregulation">ParkingSideRegulation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV25isCleanAirStickerRequiredSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isCleanAirStickerRequired" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV25isCleanAirStickerRequiredSbvp" class="token"><code>isCleanAirStickerRequired</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the country or state requires an ecological sticker. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isCleanAirStickerRequired: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV24bloodAlcoholContentLimitAA05BloodefG0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-bloodAlcoholContentLimit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV24bloodAlcoholContentLimitAA05BloodefG0Vvp" class="token"><code>bloodAlcoholContentLimit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the rules regarding alcohol in blood content limit in a country or state for all types of drivers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var bloodAlcoholContentLimit: BloodAlcoholContentLimit
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-bloodalcoholcontentlimit">BloodAlcoholContentLimit</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11tollSystemsSayAA10TollSystemVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tollSystems" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11tollSystemsSayAA10TollSystemVGvp" class="token"><code>tollSystems</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the toll systems present in a country or state.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tollSystems: [TollSystem]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-tollsystem">TollSystem</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV15preTripPlanningAA03PreeF0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-preTripPlanning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV15preTripPlanningAA03PreeF0Vvp" class="token"><code>preTripPlanning</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the legal requirements to be considered before a trip for all vehicles types.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var preTripPlanning: PreTripPlanning
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-pretripplanning">PreTripPlanning</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11countryCode05stateE014adminContextId011parentAdminH3Ids11drivingSide10unitSystem11speedLimits24timeZoneOffsetsInMinutes20daylightSavingPeriod17isUturnRestricted22headlightsRequirements14isTollRequired21isTollStickerRequired20turnOnRedRegulations07parkingN11Regulations25isCleanAirStickerRequired24bloodAlcoholContentLimit11tollSystems15preTripPlanningAcA07CountryE0O_SSSgAA0khI0VSayA_GAA07DrivingN0OSgAA04UnitP0OSgAA019GeneralVehicleSpeedR0VSaySdGAA8TimeRuleCSgSbSayAA21HeadlightsRequirementOGS2bSayAA19TurnOnRedRegulationOGSayAA07ParkingN10RegulationOGSbAA24BloodAlcoholContentLimitVSayAA04TollP0VGAA15PreTripPlanningVtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-countryCode-stateCode-adminContextId-parentAdminContextIds-drivingSide-unitSystem-speedLimits-timeZoneOffsetsInMinutes-daylightSavingPeriod-isUturnRestricted-headlightsRequirements-isTollRequired-isTollStickerRequired-turnOnRedRegulations-parkingSideRegulations-isCleanAirStickerRequired-bloodAlcoholContentLimit-tollSystems-preTripPlanning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-administrativerules#sdk-for-ios-navigate-s-7heresdk19AdministrativeRulesV11countryCode05stateE014adminContextId011parentAdminH3Ids11drivingSide10unitSystem11speedLimits24timeZoneOffsetsInMinutes20daylightSavingPeriod17isUturnRestricted22headlightsRequirements14isTollRequired21isTollStickerRequired20turnOnRedRegulations07parkingN11Regulations25isCleanAirStickerRequired24bloodAlcoholContentLimit11tollSystems15preTripPlanningAcA07CountryE0O_SSSgAA0khI0VSayA_GAA07DrivingN0OSgAA04UnitP0OSgAA019GeneralVehicleSpeedR0VSaySdGAA8TimeRuleCSgSbSayAA21HeadlightsRequirementOGS2bSayAA19TurnOnRedRegulationOGSayAA07ParkingN10RegulationOGSbAA24BloodAlcoholContentLimitVSayAA04TollP0VGAA15PreTripPlanningVtcfc" class="token"><code>init(countryCode:</code><wbr></wbr><code>stateCode:</code><wbr></wbr><code>adminContextId:</code><wbr></wbr><code>parentAdminContextIds:</code><wbr></wbr><code>drivingSide:</code><wbr></wbr><code>unitSystem:</code><wbr></wbr><code>speedLimits:</code><wbr></wbr><code>timeZoneOffsetsInMinutes:</code><wbr></wbr><code>daylightSavingPeriod:</code><wbr></wbr><code>isUturnRestricted:</code><wbr></wbr><code>headlightsRequirements:</code><wbr></wbr><code>isTollRequired:</code><wbr></wbr><code>isTollStickerRequired:</code><wbr></wbr><code>turnOnRedRegulations:</code><wbr></wbr><code>parkingSideRegulations:</code><wbr></wbr><code>isCleanAirStickerRequired:</code><wbr></wbr><code>bloodAlcoholContentLimit:</code><wbr></wbr><code>tollSystems:</code><wbr></wbr><code>preTripPlanning:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(countryCode: CountryCode = CountryCode.abw, stateCode: String? = nil, adminContextId: AdminContextId, parentAdminContextIds: [AdminContextId] = [], drivingSide: DrivingSide? = nil, unitSystem: UnitSystem? = nil, speedLimits: GeneralVehicleSpeedLimits = GeneralVehicleSpeedLimits(), timeZoneOffsetsInMinutes: [TimeInterval] = [], daylightSavingPeriod: TimeRule? = nil, isUturnRestricted: Bool = false, headlightsRequirements: [HeadlightsRequirement] = [], isTollRequired: Bool = false, isTollStickerRequired: Bool = false, turnOnRedRegulations: [TurnOnRedRegulation] = [], parkingSideRegulations: [ParkingSideRegulation] = [], isCleanAirStickerRequired: Bool = false, bloodAlcoholContentLimit: BloodAlcoholContentLimit = BloodAlcoholContentLimit(), tollSystems: [TollSystem] = [], preTripPlanning: PreTripPlanning = PreTripPlanning())
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-countrycode">CountryCode</a>
  - <a href="sdk-for-ios-navigate-structs-admincontextid">AdminContextId</a>
  - <a href="sdk-for-ios-navigate-enums-drivingside">DrivingSide</a>
  - <a href="sdk-for-ios-navigate-enums-unitsystem">UnitSystem</a>
  - <a href="sdk-for-ios-navigate-structs-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a>
  - <a href="sdk-for-ios-navigate-classes-timerule">TimeRule</a>
  - <a href="sdk-for-ios-navigate-enums-headlightsrequirement">HeadlightsRequirement</a>
  - <a href="sdk-for-ios-navigate-enums-turnonredregulation">TurnOnRedRegulation</a>
  - <a href="sdk-for-ios-navigate-enums-parkingsideregulation">ParkingSideRegulation</a>
  - <a href="sdk-for-ios-navigate-structs-bloodalcoholcontentlimit">BloodAlcoholContentLimit</a>
  - <a href="sdk-for-ios-navigate-structs-tollsystem">TollSystem</a>
  - <a href="sdk-for-ios-navigate-structs-pretripplanning">PreTripPlanning</a>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

