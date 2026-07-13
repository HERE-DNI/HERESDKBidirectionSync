---
title: "ManeuverNotificationOptions.withAllFields constructor - ManeuverNotificationOptions - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions-withallfields"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationOptions.withAllFields.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverNotificationOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ManeuverNotificationOptions.withAllFields</span> constructor

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.23.0. Use the \`withDefaults\` instead.")

</div>

<span class="name deprecated">ManeuverNotificationOptions.withAllFields</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withAllFields-param-language" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a></span> <span class="parameter-name">language</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withAllFields-param-unitSystem" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-unitsystem">UnitSystem</a></span> <span class="parameter-name">unitSystem</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withAllFields-param-includedNotificationTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType</a></span>\></span></span> <span class="parameter-name">includedNotificationTypes</span>, </span>
4.  <span id="sdk-for-flutter-navigate-withAllFields-param-enableRoundaboutNotification" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableRoundaboutNotification</span>, </span>
5.  <span id="sdk-for-flutter-navigate-withAllFields-param-enableDestinationReachedNotification" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableDestinationReachedNotification</span>, </span>
6.  <span id="sdk-for-flutter-navigate-withAllFields-param-enableDoubleNotification" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableDoubleNotification</span>, </span>
7.  <span id="sdk-for-flutter-navigate-withAllFields-param-enablePhoneme" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enablePhoneme</span>, </span>
8.  <span id="sdk-for-flutter-navigate-withAllFields-param-enableHighwayExit" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableHighwayExit</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance of this class with full specified configurations.

- `language` The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).
- `unitSystem` Defines the measurement system used for distances. Defaults to metric.
- `includedNotificationTypes` List of <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType</a> for which notifications should be generated. Excluding all of them will disable the maneuver notifications completely. By default, all types are included.
- `enableRoundaboutNotification` A flag that indicates whether notification for roundabout-related maneuvers should be generated. Defaults to `true`.
- `enableDestinationReachedNotification` A flag that indicates whether notification for destination/stopover reached maneuvers should be generated. Defaults to `true`.
- `enableDoubleNotification` A flag that indicates whether combined maneuver notifications should be generated. Such double notifications can be useful when maneuvers are very close. **Example:** A combined message: 'After 300 meters turn left and then turn right.'. This way a user can better anticipate the next-next maneuver. Note that setting to `true` will make the notification longer as two maneuvers will be merged into one. When the next-next maneuver action takes place, the notification will be given as usual. **Example:** 'Now turn left and then then turn right.' will be followed by 'Now turn right.'. Defaults to `true`.
- `enablePhoneme` A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names, road numbers, city names) should be used when generating notifications. Direction information comes usually in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of direction information sound more natural. **Note:** For now, this property is functional for road name and road number information only.

Defaults to `false`.

- `enableHighwayExit` A flag that indicates whether highway exit information should be used when generating notification. Defaults to `true`.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.23.0. Use the `withDefaults` instead.")
ManeuverNotificationOptions.withAllFields(this.language, this.unitSystem, this.includedNotificationTypes, this.enableRoundaboutNotification, this.enableDestinationReachedNotification, this.enableDoubleNotification, this.enablePhoneme, this.enableHighwayExit)
    : arrivalNotificationOption = ArrivalNotificationOption.both, notificationFormatOption = NotificationFormatOption.plain, textUsageOptions = TextUsageOptions(), enableLaneRecommendation = false, includedNaturalGuidanceTypes = [], directionInformationUsageForActionNotificationOption = DirectionInformationUsageOption.none;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
