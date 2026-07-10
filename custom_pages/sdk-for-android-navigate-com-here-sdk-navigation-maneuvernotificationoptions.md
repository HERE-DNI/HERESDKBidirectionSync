---
title: "ManeuverNotificationOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.ManeuverNotificationOptions → com.here.sdk.navigation.ManeuverNotificationOptions

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ManeuverNotificationOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class containing all options to be used when generating maneuver notifications.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-arrivalnotificationoption" title="enum class in com.here.sdk.navigation">`ArrivalNotificationOption`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#arrivalNotificationOption" class="member-name-link"><code>arrivalNotificationOption</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-directioninformationusageoption" title="enum class in com.here.sdk.navigation">`DirectionInformationUsageOption`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#directionInformationUsageForActionNotificationOption" class="member-name-link"><code>directionInformationUsageForActionNotificationOption</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  An option whether direction information should be used when generating notification with ManeuverNotificationType.ACTION .

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableDestinationReachedNotification" class="member-name-link"><code>enableDestinationReachedNotification</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated. Will be removed in v4.27.0.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableDoubleNotification" class="member-name-link"><code>enableDoubleNotification</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A flag that indicates whether combined maneuver notifications should be generated.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableHighwayExit" class="member-name-link"><code>enableHighwayExit</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A flag that indicates whether highway exit information should be used when generating notification.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableLaneRecommendation" class="member-name-link"><code>enableLaneRecommendation</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A flag that indicates whether lane recommendation should be used when generating notifications.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enablePhoneme" class="member-name-link"><code>enablePhoneme</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A flag that indicates whether phonemes in selected notification format for proper nouns (e.g.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableRoundaboutNotification" class="member-name-link"><code>enableRoundaboutNotification</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A flag that indicates whether notification for roundabout-related maneuvers should be generated.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-naturalguidancetype" title="enum class in com.here.sdk.navigation">`NaturalGuidanceType`</a>`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#includedNaturalGuidanceTypes" class="member-name-link"><code>includedNaturalGuidanceTypes</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  List of NaturalGuidanceType should be included in the notifications.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">`ManeuverNotificationType`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#includedNotificationTypes" class="member-name-link"><code>includedNotificationTypes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of ManeuverNotificationType for which notifications should be generated.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">`LanguageCode`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#language" class="member-name-link"><code>language</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The language in which the notifications will be generated.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-notificationformatoption" title="enum class in com.here.sdk.navigation">`NotificationFormatOption`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#notificationFormatOption" class="member-name-link"><code>notificationFormatOption</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A formatting option for the phoneme that is included in the notification.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-textusageoptions" title="class in com.here.sdk.routing">`TextUsageOptions`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#textUsageOptions" class="member-name-link"><code>textUsageOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  An option whether street name, road number and sign post direction should be used when generating notification.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">`UnitSystem`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#unitSystem" class="member-name-link"><code>unitSystem</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines the measurement system used for distances.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      ManeuverNotificationOptions ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class with default configurations.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      ManeuverNotificationOptions ( LanguageCode language, UnitSystem unitSystem)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated. Will be removed in v4.23.0.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      ManeuverNotificationOptions ( LanguageCode language, UnitSystem unitSystem, List < ManeuverNotificationType > includedNotificationTypes,
       boolean enableRoundaboutNotification,
       boolean enableDestinationReachedNotification,
       boolean enableDoubleNotification,
       boolean enablePhoneme,
       boolean enableHighwayExit)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated. Will be removed in v4.23.0.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      ManeuverNotificationOptions ( LanguageCode language, UnitSystem unitSystem, List < ManeuverNotificationType > includedNotificationTypes,
       boolean enableRoundaboutNotification,
       boolean enableDestinationReachedNotification,
       boolean enableDoubleNotification,
       boolean enablePhoneme, NotificationFormatOption notificationFormatOption,
       boolean enableHighwayExit)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated. Will be removed in v4.23.0.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      ManeuverNotificationOptions ( LanguageCode language, UnitSystem unitSystem, List < ManeuverNotificationType > includedNotificationTypes,
       boolean enableRoundaboutNotification,
       boolean enableDestinationReachedNotification,
       boolean enableDoubleNotification,
       boolean enablePhoneme, TextUsageOptions textUsageOptions,
       boolean enableHighwayExit)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated. Will be removed in v4.23.0.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-language" class="section detail">

    ### language

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></span> <span class="element-name">language</span>

    </div>

    <div class="block">

    The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-unitSystem" class="section detail">

    ### unitSystem

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></span> <span class="element-name">unitSystem</span>

    </div>

    <div class="block">

    Defines the measurement system used for distances. Defaults to metric.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-includedNotificationTypes" class="section detail">

    ### includedNotificationTypes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>\></span> <span class="element-name">includedNotificationTypes</span>

    </div>

    <div class="block">

    List of ManeuverNotificationType for which notifications should be generated. Excluding all of them will disable the maneuver notifications completely. By default, all types are included.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-enableRoundaboutNotification" class="section detail">

    ### enableRoundaboutNotification

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableRoundaboutNotification</span>

    </div>

    <div class="block">

    A flag that indicates whether notification for roundabout-related maneuvers should be generated. Defaults to true .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-enableDestinationReachedNotification" class="section detail">

    ### enableDestinationReachedNotification

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableDestinationReachedNotification</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.27.0. Use the <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#arrivalNotificationOption">`arrivalNotificationOption`</a> instead

    </div>

    </div>

    <div class="block">

    A flag that indicates whether notification for destination/stopover reached maneuvers should be generated. Defaults to true .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-arrivalNotificationOption" class="section detail">

    ### arrivalNotificationOption

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-arrivalnotificationoption" title="enum class in com.here.sdk.navigation">ArrivalNotificationOption</a></span> <span class="element-name">arrivalNotificationOption</span>

    </div>

    <div class="block">

    A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated. Defaults to ArrivalNotificationOption.BOTH .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-enableDoubleNotification" class="section detail">

    ### enableDoubleNotification

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableDoubleNotification</span>

    </div>

    <div class="block">

    A flag that indicates whether combined maneuver notifications should be generated. Such double notifications can be useful when maneuvers are very close. Example: A combined message: 'After 300 meters turn left and then turn right.'. This way a user can better anticipate the next-next maneuver. Note that setting to true will make the notification longer as two maneuvers will be merged into one. When the next-next maneuver action takes place, the notification will be given as usual. Example: 'Now turn left and then then turn right.' will be followed by 'Now turn right.'. Defaults to true .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-enablePhoneme" class="section detail">

    ### enablePhoneme

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enablePhoneme</span>

    </div>

    <div class="block">

    A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names, road numbers, city names) should be used when generating notifications. Direction information comes usually in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of direction information sound more natural. Note: For now, this property is functional for road name and road number information only. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-notificationFormatOption" class="section detail">

    ### notificationFormatOption

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a></span> <span class="element-name">notificationFormatOption</span>

    </div>

    <div class="block">

    A formatting option for the phoneme that is included in the notification. By default, no phoneme is used and the NotificationFormatOption.PLAIN orthographic form is included in the notification. Note: To use the SSML format for phonemes, enablePhoneme needs to be set to true .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-textUsageOptions" class="section detail">

    ### textUsageOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a></span> <span class="element-name">textUsageOptions</span>

    </div>

    <div class="block">

    An option whether street name, road number and sign post direction should be used when generating notification. Defaults to each attribute as LocalizedTextPreference.USE_ALWAYS .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-enableHighwayExit" class="section detail">

    ### enableHighwayExit

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableHighwayExit</span>

    </div>

    <div class="block">

    A flag that indicates whether highway exit information should be used when generating notification. Defaults to true .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-enableLaneRecommendation" class="section detail">

    ### enableLaneRecommendation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableLaneRecommendation</span>

    </div>

    <div class="block">

    A flag that indicates whether lane recommendation should be used when generating notifications. In case the flag is enabled, only the notification for the ManeuverNotificationType.DISTANCE maneuver notification type will contain the lane recommendation. The lane recommandation will replace the direction information in the notification. Example: 'After 250 meters use the right two lanes and turn right.'. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-includedNaturalGuidanceTypes" class="section detail">

    ### includedNaturalGuidanceTypes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-naturalguidancetype" title="enum class in com.here.sdk.navigation">NaturalGuidanceType</a>\></span> <span class="element-name">includedNaturalGuidanceTypes</span>

    </div>

    <div class="block">

    List of NaturalGuidanceType should be included in the notifications. Excluding all of them will disable natural guidance information in the notifications completely. By default, the list is empty and natural guidance is disabled.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-directionInformationUsageForActionNotificationOption" class="section detail">

    ### directionInformationUsageForActionNotificationOption

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-directioninformationusageoption" title="enum class in com.here.sdk.navigation">DirectionInformationUsageOption</a></span> <span class="element-name">directionInformationUsageForActionNotificationOption</span>

    </div>

    <div class="block">

    An option whether direction information should be used when generating notification with ManeuverNotificationType.ACTION . Defaults to DirectionInformationUsageOption.NONE .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### ManeuverNotificationOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span>()

    </div>

    <div class="block">

    Creates a new instance of this class with default configurations.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-LanguageCode-com-here-sdk-core-UnitSystem" class="section detail">

    ### ManeuverNotificationOptions

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.23.0. Use the default constructor instead.

    </div>

    </div>

    <div class="block">

    Creates a new instance of this class with specified language and unit system.

    </div>

    Parameters:  
    `language` -

    The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).

    `unitSystem` -

    Defines the measurement system used for distances. Defaults to metric.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-LanguageCode-com-here-sdk-core-UnitSystem-java-util-List-boolean-boolean-boolean-boolean-com-here-sdk-routing-TextUsageOptions-boolean" class="section detail">

    ### ManeuverNotificationOptions

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>\> includedNotificationTypes, boolean enableRoundaboutNotification, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> boolean enableDestinationReachedNotification, boolean enableDoubleNotification, boolean enablePhoneme, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a> textUsageOptions, boolean enableHighwayExit)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.23.0. Use the default constructor instead.

    </div>

    </div>

    <div class="block">

    Creates a new instance of this class with full specified configurations.

    </div>

    Parameters:  
    `language` -

    The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).

    `unitSystem` -

    Defines the measurement system used for distances. Defaults to metric.

    `includedNotificationTypes` -

    List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">`ManeuverNotificationType`</a> for which notifications should be generated. Excluding all of them will disable the maneuver notifications completely. By default, all types are included.

    `enableRoundaboutNotification` -

    A flag that indicates whether notification for roundabout-related maneuvers should be generated. Defaults to `true`.

    `enableDestinationReachedNotification` -

    A flag that indicates whether notification for destination/stopover reached maneuvers should be generated. Defaults to `true`.

    `enableDoubleNotification` -

    A flag that indicates whether combined maneuver notifications should be generated. Such double notifications can be useful when maneuvers are very close. **Example:** A combined message: 'After 300 meters turn left and then turn right.'. This way a user can better anticipate the next-next maneuver. Note that setting to `true` will make the notification longer as two maneuvers will be merged into one. When the next-next maneuver action takes place, the notification will be given as usual. **Example:** 'Now turn left and then then turn right.' will be followed by 'Now turn right.'. Defaults to `true`.

    `enablePhoneme` -

    A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names, road numbers, city names) should be used when generating notifications. Direction information comes usually in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of direction information sound more natural. **Note:** For now, this property is functional for road name and road number information only. Defaults to `false`.

    `textUsageOptions` -

    An option whether street name, road number and sign post direction should be used when generating notification. Defaults to each attribute as <a href="sdk-for-android-navigate-com-here-sdk-routing-localizedtextpreference#USE_ALWAYS">`LocalizedTextPreference.USE_ALWAYS`</a>.

    `enableHighwayExit` -

    A flag that indicates whether highway exit information should be used when generating notification. Defaults to `true`.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-LanguageCode-com-here-sdk-core-UnitSystem-java-util-List-boolean-boolean-boolean-boolean-boolean" class="section detail">

    ### ManeuverNotificationOptions

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>\> includedNotificationTypes, boolean enableRoundaboutNotification, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> boolean enableDestinationReachedNotification, boolean enableDoubleNotification, boolean enablePhoneme, boolean enableHighwayExit)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.23.0. Use the default constructor instead.

    </div>

    </div>

    <div class="block">

    Creates a new instance of this class with full specified configurations.

    </div>

    Parameters:  
    `language` -

    The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).

    `unitSystem` -

    Defines the measurement system used for distances. Defaults to metric.

    `includedNotificationTypes` -

    List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">`ManeuverNotificationType`</a> for which notifications should be generated. Excluding all of them will disable the maneuver notifications completely. By default, all types are included.

    `enableRoundaboutNotification` -

    A flag that indicates whether notification for roundabout-related maneuvers should be generated. Defaults to `true`.

    `enableDestinationReachedNotification` -

    A flag that indicates whether notification for destination/stopover reached maneuvers should be generated. Defaults to `true`.

    `enableDoubleNotification` -

    A flag that indicates whether combined maneuver notifications should be generated. Such double notifications can be useful when maneuvers are very close. **Example:** A combined message: 'After 300 meters turn left and then turn right.'. This way a user can better anticipate the next-next maneuver. Note that setting to `true` will make the notification longer as two maneuvers will be merged into one. When the next-next maneuver action takes place, the notification will be given as usual. **Example:** 'Now turn left and then then turn right.' will be followed by 'Now turn right.'. Defaults to `true`.

    `enablePhoneme` -

    A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names, road numbers, city names) should be used when generating notifications. Direction information comes usually in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of direction information sound more natural. **Note:** For now, this property is functional for road name and road number information only. Defaults to `false`.

    `enableHighwayExit` -

    A flag that indicates whether highway exit information should be used when generating notification. Defaults to `true`.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-LanguageCode-com-here-sdk-core-UnitSystem-java-util-List-boolean-boolean-boolean-boolean-com-here-sdk-navigation-NotificationFormatOption-boolean" class="section detail">

    ### ManeuverNotificationOptions

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>\> includedNotificationTypes, boolean enableRoundaboutNotification, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> boolean enableDestinationReachedNotification, boolean enableDoubleNotification, boolean enablePhoneme, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a> notificationFormatOption, boolean enableHighwayExit)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.23.0. Use the default constructor instead.

    </div>

    </div>

    <div class="block">

    Creates a new instance of this class with full specified configurations.

    </div>

    Parameters:  
    `language` -

    The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).

    `unitSystem` -

    Defines the measurement system used for distances. Defaults to metric.

    `includedNotificationTypes` -

    List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">`ManeuverNotificationType`</a> for which notifications should be generated. Excluding all of them will disable the maneuver notifications completely. By default, all types are included.

    `enableRoundaboutNotification` -

    A flag that indicates whether notification for roundabout-related maneuvers should be generated. Defaults to `true`.

    `enableDestinationReachedNotification` -

    A flag that indicates whether notification for destination/stopover reached maneuvers should be generated. Defaults to `true`.

    `enableDoubleNotification` -

    A flag that indicates whether combined maneuver notifications should be generated. Such double notifications can be useful when maneuvers are very close. **Example:** A combined message: 'After 300 meters turn left and then turn right.'. This way a user can better anticipate the next-next maneuver. Note that setting to `true` will make the notification longer as two maneuvers will be merged into one. When the next-next maneuver action takes place, the notification will be given as usual. **Example:** 'Now turn left and then then turn right.' will be followed by 'Now turn right.'. Defaults to `true`.

    `enablePhoneme` -

    A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names, road numbers, city names) should be used when generating notifications. Direction information comes usually in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of direction information sound more natural. **Note:** For now, this property is functional for road name and road number information only. Defaults to `false`.

    `notificationFormatOption` -

    A formatting option for the phoneme that is included in the notification. By default, no phoneme is used and the <a href="sdk-for-android-navigate-com-here-sdk-navigation-notificationformatoption#PLAIN">`NotificationFormatOption.PLAIN`</a> orthographic form is included in the notification. **Note:** To use the SSML format for phonemes, <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enablePhoneme">`enablePhoneme`</a> needs to be set to `true`.

    `enableHighwayExit` -

    A flag that indicates whether highway exit information should be used when generating notification. Defaults to `true`.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

