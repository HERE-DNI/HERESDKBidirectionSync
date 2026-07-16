---
title: "ManeuverNotificationOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-maneuvernotificationoptions"
---

# ManeuverNotificationOptions

<div class="declaration">

<div class="language">

``` highlight
public struct ManeuverNotificationOptions : Hashable
```

</div>

</div>

A struct containing all options to be used when generating maneuver notifications.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8languageAA12LanguageCodeOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-language" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8languageAA12LanguageCodeOvp" class="token"><code>language</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var language: LanguageCode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV10unitSystemAA04UnitF0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-unitSystem" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV10unitSystemAA04UnitF0Ovp" class="token"><code>unitSystem</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the measurement system used for distances. Defaults to metric.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var unitSystem: UnitSystem
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-unitsystem">UnitSystem</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV08includedC5TypesSayAA0bC4TypeOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-includedNotificationTypes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV08includedC5TypesSayAA0bC4TypeOGvp" class="token"><code>includedNotificationTypes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">`ManeuverNotificationType`</a> for which notifications should be generated. Excluding all of them will disable the maneuver notifications completely. By default, all types are included.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var includedNotificationTypes: [ManeuverNotificationType]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">ManeuverNotificationType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV016enableRoundaboutC0Sbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-enableRoundaboutNotification" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV016enableRoundaboutC0Sbvp" class="token"><code>enableRoundaboutNotification</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether notification for roundabout-related maneuvers should be generated. Defaults to `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var enableRoundaboutNotification: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV024enableDestinationReachedC0Sbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-enableDestinationReachedNotification" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV024enableDestinationReachedC0Sbvp" class="token"><code>enableDestinationReachedNotification</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether notification for destination/stopover reached maneuvers should be generated. Defaults to `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.27.0. Use the `ManeuverNotificationOptions.arrivalNotificationOption` instead")
  public var enableDestinationReachedNotification: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV07arrivalC6OptionAA07ArrivalcF0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-arrivalNotificationOption" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV07arrivalC6OptionAA07ArrivalcF0Ovp" class="token"><code>arrivalNotificationOption</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated. Defaults to `ArrivalNotificationOption.BOTH`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var arrivalNotificationOption: ArrivalNotificationOption
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-arrivalnotificationoption">ArrivalNotificationOption</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV012enableDoubleC0Sbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-enableDoubleNotification" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV012enableDoubleC0Sbvp" class="token"><code>enableDoubleNotification</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether combined maneuver notifications should be generated. Such double notifications can be useful when maneuvers are very close. **Example:** A combined message: ‘After 300 meters turn left and then turn right.’. This way a user can better anticipate the next-next maneuver. Note that setting to `true` will make the notification longer as two maneuvers will be merged into one. When the next-next maneuver action takes place, the notification will be given as usual. **Example:** ‘Now turn left and then then turn right.’ will be followed by ‘Now turn right.’. Defaults to `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var enableDoubleNotification: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV13enablePhonemeSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-enablePhoneme" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV13enablePhonemeSbvp" class="token"><code>enablePhoneme</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names, road numbers, city names) should be used when generating notifications. Direction information comes usually in orthographic form and phoneme (e.g. Wall Street and “wɔːl"striːt). However, when the notification is synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of direction information sound more natural. **Note:** For now, this property is functional for road name and road number information only. Moreover, the native `AVSpeechSynthesizer` for iOS does not support phonemes as of now. Other 3rd party TTS engines may support it. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var enablePhoneme: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV24notificationFormatOptionAA0cfG0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-notificationFormatOption" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV24notificationFormatOptionAA0cfG0Ovp" class="token"><code>notificationFormatOption</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A formatting option for the phoneme that is included in the notification. By default, no phoneme is used and the <a href="sdk-for-ios-navigate-enums-notificationformatoption#sdk-for-ios-navigate-s-7heresdk24NotificationFormatOptionO5plainyA2CmF">`NotificationFormatOption.plain`</a> orthographic form is included in the notification.

  **Note:** To use the SSML format for phonemes, <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV13enablePhonemeSbvp">`ManeuverNotificationOptions.enablePhoneme`</a> needs to be set to `true`. Moreover, the SSML format is not supported by the native `AVSpeechSynthesizer` for iOS, as of now. Other 3rd party TTS engines may support it.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var notificationFormatOption: NotificationFormatOption
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-notificationformatoption">NotificationFormatOption</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV09textUsageD0AA04TextfD0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-textUsageOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV09textUsageD0AA04TextfD0Vvp" class="token"><code>textUsageOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An option whether street name, road number and sign post direction should be used when generating notification. Defaults to each attribute as <a href="sdk-for-ios-navigate-enums-localizedtextpreference#sdk-for-ios-navigate-s-7heresdk23LocalizedTextPreferenceO9useAlwaysyA2CmF">`LocalizedTextPreference.useAlways`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textUsageOptions: TextUsageOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-textusageoptions">TextUsageOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV17enableHighwayExitSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-enableHighwayExit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV17enableHighwayExitSbvp" class="token"><code>enableHighwayExit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether highway exit information should be used when generating notification. Defaults to `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var enableHighwayExit: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV24enableLaneRecommendationSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-enableLaneRecommendation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV24enableLaneRecommendationSbvp" class="token"><code>enableLaneRecommendation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A flag that indicates whether lane recommendation should be used when generating notifications. In case the flag is enabled, *only* the notification for the <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#sdk-for-ios-navigate-s-7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">`ManeuverNotificationType.distance`</a> maneuver notification type will contain the lane recommendation. The lane recommandation will replace the direction information in the notification. **Example:** ‘After 250 meters use the right two lanes and turn right.’. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var enableLaneRecommendation: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV28includedNaturalGuidanceTypesSayAA0fG4TypeOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-includedNaturalGuidanceTypes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV28includedNaturalGuidanceTypesSayAA0fG4TypeOGvp" class="token"><code>includedNaturalGuidanceTypes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of <a href="sdk-for-ios-navigate-enums-naturalguidancetype">`NaturalGuidanceType`</a> should be included in the notifications. Excluding all of them will disable natural guidance information in the notifications completely.

  By default, the list is empty and natural guidance is disabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var includedNaturalGuidanceTypes: [NaturalGuidanceType]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-naturalguidancetype">NaturalGuidanceType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV034directionInformationUsageForActionC6OptionAA09DirectionfgJ0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-directionInformationUsageForActionNotificationOption" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV034directionInformationUsageForActionC6OptionAA09DirectionfgJ0Ovp" class="token"><code>directionInformationUsageForActionNotificationOption</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An option whether direction information should be used when generating notification with <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype#sdk-for-ios-navigate-s-7heresdk24ManeuverNotificationTypeO6actionyA2CmF">`ManeuverNotificationType.action`</a>. Defaults to <a href="sdk-for-ios-navigate-enums-directioninformationusageoption#sdk-for-ios-navigate-s-7heresdk31DirectionInformationUsageOptionO4noneyA2CmF">`DirectionInformationUsageOption.none`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var directionInformationUsageForActionNotificationOption: DirectionInformationUsageOption
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-directioninformationusageoption">DirectionInformationUsageOption</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsVACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsVACycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class with default configurations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8language10unitSystemAcA12LanguageCodeO_AA04UnitG0Otcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-language-unitSystem" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8language10unitSystemAcA12LanguageCodeO_AA04UnitG0Otcfc" class="token"><code>init(language:</code><wbr></wbr><code>unitSystem:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class with specified language and unit system.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.23.0. Use the default constructor instead.")
  public init(language: LanguageCode, unitSystem: UnitSystem)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-navigate-enums-unitsystem">UnitSystem</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme09textUsageD00J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS4bAA04TextqD0VSbtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-language-unitSystem-includedNotificationTypes-enableRoundaboutNotification-enableDestinationReachedNotification-enableDoubleNotification-enablePhoneme-textUsageOptions-enableHighwayExit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme09textUsageD00J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS4bAA04TextqD0VSbtcfc" class="token"><code>init(language:</code><wbr></wbr><code>unitSystem:</code><wbr></wbr><code>includedNotificationTypes:</code><wbr></wbr><code>enableRoundaboutNotification:</code><wbr></wbr><code>enableDestinationReachedNotification:</code><wbr></wbr><code>enableDoubleNotification:</code><wbr></wbr><code>enablePhoneme:</code><wbr></wbr><code>textUsageOptions:</code><wbr></wbr><code>enableHighwayExit:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class with full specified configurations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.23.0. Use the default constructor instead.")
  public init(language: LanguageCode, unitSystem: UnitSystem, includedNotificationTypes: [ManeuverNotificationType], enableRoundaboutNotification: Bool, enableDestinationReachedNotification: Bool, enableDoubleNotification: Bool, enablePhoneme: Bool, textUsageOptions: TextUsageOptions, enableHighwayExit: Bool)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-navigate-enums-unitsystem">UnitSystem</a>
  - <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">ManeuverNotificationType</a>
  - <a href="sdk-for-ios-navigate-structs-textusageoptions">TextUsageOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme0J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS5btcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-language-unitSystem-includedNotificationTypes-enableRoundaboutNotification-enableDestinationReachedNotification-enableDoubleNotification-enablePhoneme-enableHighwayExit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme0J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS5btcfc" class="token"><code>init(language:</code><wbr></wbr><code>unitSystem:</code><wbr></wbr><code>includedNotificationTypes:</code><wbr></wbr><code>enableRoundaboutNotification:</code><wbr></wbr><code>enableDestinationReachedNotification:</code><wbr></wbr><code>enableDoubleNotification:</code><wbr></wbr><code>enablePhoneme:</code><wbr></wbr><code>enableHighwayExit:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class with full specified configurations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.23.0. Use the default constructor instead.")
  public init(language: LanguageCode, unitSystem: UnitSystem, includedNotificationTypes: [ManeuverNotificationType], enableRoundaboutNotification: Bool, enableDestinationReachedNotification: Bool, enableDoubleNotification: Bool, enablePhoneme: Bool, enableHighwayExit: Bool)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-navigate-enums-unitsystem">UnitSystem</a>
  - <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">ManeuverNotificationType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme24notificationFormatOption0J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS4bAA0cqR0OSbtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-language-unitSystem-includedNotificationTypes-enableRoundaboutNotification-enableDestinationReachedNotification-enableDoubleNotification-enablePhoneme-notificationFormatOption-enableHighwayExit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV8language10unitSystem08includedC5Types016enableRoundaboutC00j18DestinationReachedC00j6DoubleC00J7Phoneme24notificationFormatOption0J11HighwayExitAcA12LanguageCodeO_AA04UnitG0OSayAA0bC4TypeOGS4bAA0cqR0OSbtcfc" class="token"><code>init(language:</code><wbr></wbr><code>unitSystem:</code><wbr></wbr><code>includedNotificationTypes:</code><wbr></wbr><code>enableRoundaboutNotification:</code><wbr></wbr><code>enableDestinationReachedNotification:</code><wbr></wbr><code>enableDoubleNotification:</code><wbr></wbr><code>enablePhoneme:</code><wbr></wbr><code>notificationFormatOption:</code><wbr></wbr><code>enableHighwayExit:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class with full specified configurations.

  - Parameters

    - language: The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).
    - unitSystem: Defines the measurement system used for distances. Defaults to metric.
    - includedNotificationTypes: List of <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">`ManeuverNotificationType`</a> for which notifications should be generated. Excluding all of them will disable the maneuver notifications completely. By default, all types are included.
    - enableRoundaboutNotification: A flag that indicates whether notification for roundabout-related maneuvers should be generated. Defaults to `true`.
    - enableDestinationReachedNotification: A flag that indicates whether notification for destination/stopover reached maneuvers should be generated. Defaults to `true`.
    - enableDoubleNotification: A flag that indicates whether combined maneuver notifications should be generated. Such double notifications can be useful when maneuvers are very close. **Example:** A combined message: ‘After 300 meters turn left and then turn right.’. This way a user can better anticipate the next-next maneuver. Note that setting to `true` will make the notification longer as two maneuvers will be merged into one. When the next-next maneuver action takes place, the notification will be given as usual. **Example:** ‘Now turn left and then then turn right.’ will be followed by ‘Now turn right.’. Defaults to `true`.
    - enablePhoneme: A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names, road numbers, city names) should be used when generating notifications. Direction information comes usually in orthographic form and phoneme (e.g. Wall Street and “wɔːl"striːt). However, when the notification is synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of direction information sound more natural. **Note:** For now, this property is functional for road name and road number information only. Moreover, the native `AVSpeechSynthesizer` for iOS does not support phonemes as of now. Other 3rd party TTS engines may support it. Defaults to `false`.
    - notificationFormatOption: A formatting option for the phoneme that is included in the notification. By default, no phoneme is used and the <a href="sdk-for-ios-navigate-enums-notificationformatoption#sdk-for-ios-navigate-s-7heresdk24NotificationFormatOptionO5plainyA2CmF">`NotificationFormatOption.plain`</a> orthographic form is included in the notification.

    **Note:** To use the SSML format for phonemes, <a href="sdk-for-ios-navigate-structs-maneuvernotificationoptions#sdk-for-ios-navigate-s-7heresdk27ManeuverNotificationOptionsV13enablePhonemeSbvp">`ManeuverNotificationOptions.enablePhoneme`</a> needs to be set to `true`. Moreover, the SSML format is not supported by the native `AVSpeechSynthesizer` for iOS, as of now. Other 3rd party TTS engines may support it.

    - enableHighwayExit: A flag that indicates whether highway exit information should be used when generating notification. Defaults to `true`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.23.0. Use the default constructor instead.")
  public init(language: LanguageCode, unitSystem: UnitSystem, includedNotificationTypes: [ManeuverNotificationType], enableRoundaboutNotification: Bool, enableDestinationReachedNotification: Bool, enableDoubleNotification: Bool, enablePhoneme: Bool, notificationFormatOption: NotificationFormatOption, enableHighwayExit: Bool)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-navigate-enums-unitsystem">UnitSystem</a>
  - <a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">ManeuverNotificationType</a>
  - <a href="sdk-for-ios-navigate-enums-notificationformatoption">NotificationFormatOption</a>

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

