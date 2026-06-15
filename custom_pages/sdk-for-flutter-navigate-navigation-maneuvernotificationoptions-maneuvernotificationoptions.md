---
title: "ManeuverNotificationOptions constructor"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationOptions.html -->


<div>
<h1>ManeuverNotificationOptions constructor</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.23.0. Use the withDefaults instead.")</li>
</ol>
</div>
ManeuverNotificationOptions(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a> language, </li>
<li><a href="sdk-for-flutter-navigate-core-unitsystem">UnitSystem</a> unitSystem</li>
</ol>)
    

<p>Creates a new instance of this class with specified language and unit system.</p>
<ul>
<li><code>language</code> The language in which the notifications will be generated. When the specified language
is not supported, the default language is used, which is English (American).</li>
<li><code>unitSystem</code> Defines the measurement system used for distances. Defaults to metric.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.23.0. Use the withDefaults instead.")
ManeuverNotificationOptions(this.language, this.unitSystem)
    : includedNotificationTypes = [ManeuverNotificationType.range, ManeuverNotificationType.reminder, ManeuverNotificationType.distance, ManeuverNotificationType.action], enableRoundaboutNotification = true, enableDestinationReachedNotification = true, arrivalNotificationOption = ArrivalNotificationOption.both, enableDoubleNotification = true, enablePhoneme = false, notificationFormatOption = NotificationFormatOption.plain, textUsageOptions = TextUsageOptions(), enableHighwayExit = true, enableLaneRecommendation = false, includedNaturalGuidanceTypes = [], directionInformationUsageForActionNotificationOption = DirectionInformationUsageOption.none;</code></pre>

 



</div>
`
}</HTMLBlock>
