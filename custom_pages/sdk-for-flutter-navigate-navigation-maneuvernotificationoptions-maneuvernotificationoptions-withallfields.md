---
title: "ManeuverNotificationOptions.withAllFields constructor"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-maneuvernotificationoptions-withallfields"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationOptions.withAllFields.html -->


<div>
<h1>ManeuverNotificationOptions.withAllFields constructor</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.23.0. Use the withDefaults instead.")</li>
</ol>
</div>
ManeuverNotificationOptions.withAllFields(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a> language, </li>
<li><a href="sdk-for-flutter-navigate-core-unitsystem">UnitSystem</a> unitSystem, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType</a>&gt; includedNotificationTypes, </li>
<li>bool enableRoundaboutNotification, </li>
<li>bool enableDestinationReachedNotification, </li>
<li>bool enableDoubleNotification, </li>
<li>bool enablePhoneme, </li>
<li>bool enableHighwayExit, </li>
</ol>)
    

<p>Creates a new instance of this class with full specified configurations.</p>
<ul>
<li><code>language</code> The language in which the notifications will be generated. When the specified language
is not supported, the default language is used, which is English (American).</li>
<li><code>unitSystem</code> Defines the measurement system used for distances. Defaults to metric.</li>
<li><code>includedNotificationTypes</code> List of <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType</a> for which notifications should be generated. Excluding all of
them will disable the maneuver notifications completely.
By default, all types are included.</li>
<li><code>enableRoundaboutNotification</code> A flag that indicates whether notification for roundabout-related maneuvers should be generated.
Defaults to <code>true</code>.</li>
<li><code>enableDestinationReachedNotification</code> A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
Defaults to <code>true</code>.</li>
<li><code>enableDoubleNotification</code> A flag that indicates whether combined maneuver notifications should be generated.
Such double notifications can be useful when maneuvers are very close.
<strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'.
This way a user can better anticipate the next-next maneuver.
Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
When the next-next maneuver action takes place, the notification will be given as usual.
<strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'.
Defaults to <code>true</code>.</li>
<li><code>enablePhoneme</code> A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
road numbers, city names) should be used when generating notifications. Direction information comes usually
in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is
synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
direction information sound more natural.
<strong>Note:</strong> For now, this property is functional for road name and road number information only.</li>
</ul>
<p>Defaults to <code>false</code>.</p>
<ul>
<li><code>enableHighwayExit</code> A flag that indicates whether highway exit information should be used when generating notification.
Defaults to <code>true</code>.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.23.0. Use the withDefaults instead.")
ManeuverNotificationOptions.withAllFields(this.language, this.unitSystem, this.includedNotificationTypes, this.enableRoundaboutNotification, this.enableDestinationReachedNotification, this.enableDoubleNotification, this.enablePhoneme, this.enableHighwayExit)
    : arrivalNotificationOption = ArrivalNotificationOption.both, notificationFormatOption = NotificationFormatOption.plain, textUsageOptions = TextUsageOptions(), enableLaneRecommendation = false, includedNaturalGuidanceTypes = [], directionInformationUsageForActionNotificationOption = DirectionInformationUsageOption.none;</code></pre>

 



</div>
`
}</HTMLBlock>
