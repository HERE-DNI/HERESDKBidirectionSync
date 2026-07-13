---
title: "ManeuverNotificationOptions constructor - ManeuverNotificationOptions - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverNotificationOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ManeuverNotificationOptions</span> constructor

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.23.0. Use the \`withDefaults\` instead.")

</div>

<span class="name deprecated">ManeuverNotificationOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-language" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a></span> <span class="parameter-name">language</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-unitSystem" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-unitsystem">UnitSystem</a></span> <span class="parameter-name">unitSystem</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance of this class with specified language and unit system.

- `language` The language in which the notifications will be generated. When the specified language is not supported, the default language is used, which is English (American).
- `unitSystem` Defines the measurement system used for distances. Defaults to metric.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.23.0. Use the `withDefaults` instead.")
ManeuverNotificationOptions(this.language, this.unitSystem)
    : includedNotificationTypes = [ManeuverNotificationType.range, ManeuverNotificationType.reminder, ManeuverNotificationType.distance, ManeuverNotificationType.action], enableRoundaboutNotification = true, enableDestinationReachedNotification = true, arrivalNotificationOption = ArrivalNotificationOption.both, enableDoubleNotification = true, enablePhoneme = false, notificationFormatOption = NotificationFormatOption.plain, textUsageOptions = TextUsageOptions(), enableHighwayExit = true, enableLaneRecommendation = false, includedNaturalGuidanceTypes = [], directionInformationUsageForActionNotificationOption = DirectionInformationUsageOption.none;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
