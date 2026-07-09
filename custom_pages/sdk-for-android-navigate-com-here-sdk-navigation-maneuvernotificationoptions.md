---
title: "ManeuverNotificationOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ManeuverNotificationOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.ManeuverNotificationOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ManeuverNotificationOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class containing all options to be used when generating maneuver notifications.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-arrivalnotificationoption" title="enum class in com.here.sdk.navigation">ArrivalNotificationOption</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#arrivalNotificationOption">arrivalNotificationOption</a></code></div>
<div className="col-last even-row-color">
<div className="block">A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-directioninformationusageoption" title="enum class in com.here.sdk.navigation">DirectionInformationUsageOption</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#directionInformationUsageForActionNotificationOption">directionInformationUsageForActionNotificationOption</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An option whether direction information should be used when generating notification with
 <a href="sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a>.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableDestinationReachedNotification">enableDestinationReachedNotification</a></code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableDoubleNotification">enableDoubleNotification</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A flag that indicates whether combined maneuver notifications should be generated.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableHighwayExit">enableHighwayExit</a></code></div>
<div className="col-last even-row-color">
<div className="block">A flag that indicates whether highway exit information should be used when generating notification.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableLaneRecommendation">enableLaneRecommendation</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A flag that indicates whether lane recommendation should be used when generating notifications.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enablePhoneme">enablePhoneme</a></code></div>
<div className="col-last even-row-color">
<div className="block">A flag that indicates whether phonemes in selected notification format for proper nouns (e.g.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enableRoundaboutNotification">enableRoundaboutNotification</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A flag that indicates whether notification for roundabout-related maneuvers should be generated.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-naturalguidancetype" title="enum class in com.here.sdk.navigation">NaturalGuidanceType</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#includedNaturalGuidanceTypes">includedNaturalGuidanceTypes</a></code></div>
<div className="col-last even-row-color">
<div className="block">List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-naturalguidancetype" title="enum class in com.here.sdk.navigation"><code>NaturalGuidanceType</code></a> should be included in the notifications.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#includedNotificationTypes">includedNotificationTypes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#language">language</a></code></div>
<div className="col-last even-row-color">
<div className="block">The language in which the notifications will be generated.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#notificationFormatOption">notificationFormatOption</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A formatting option for the phoneme that is included in the notification.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#textUsageOptions">textUsageOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">An option whether street name, road number and sign post direction should be used when generating notification.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#unitSystem">unitSystem</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Defines the measurement system used for distances.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#%3Cinit%3E()">ManeuverNotificationOptions</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class with default configurations.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#%3Cinit%3E(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem)">ManeuverNotificationOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem)</code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment">Will be removed in v4.23.0.</div>
</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#%3Cinit%3E(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,boolean)">ManeuverNotificationOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 boolean enableHighwayExit)</code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment">Will be removed in v4.23.0.</div>
</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#%3Cinit%3E(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,com.here.sdk.navigation.NotificationFormatOption,boolean)">ManeuverNotificationOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a> notificationFormatOption,
 boolean enableHighwayExit)</code></div>
<div className="col-last odd-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment">Will be removed in v4.23.0.</div>
</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#%3Cinit%3E(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,com.here.sdk.routing.TextUsageOptions,boolean)">ManeuverNotificationOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a> textUsageOptions,
 boolean enableHighwayExit)</code></div>
<div className="col-last even-row-color">
<div className="block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment">Will be removed in v4.23.0.</div>
</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="language">
<h3>language</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></span> <span className="element-name">language</span></div>
<div className="block"><p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></div>
</section>
</li>
<li>
<section className="detail" id="unitSystem">
<h3>unitSystem</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></span> <span className="element-name">unitSystem</span></div>
<div className="block"><p>Defines the measurement system used for distances. Defaults to metric.</p></div>
</section>
</li>
<li>
<section className="detail" id="includedNotificationTypes">
<h3>includedNotificationTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt;</span> <span className="element-name">includedNotificationTypes</span></div>
<div className="block"><p>List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated. Excluding all of
 them will disable the maneuver notifications completely.
 By default, all types are included.</p></div>
</section>
</li>
<li>
<section className="detail" id="enableRoundaboutNotification">
<h3>enableRoundaboutNotification</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enableRoundaboutNotification</span></div>
<div className="block"><p>A flag that indicates whether notification for roundabout-related maneuvers should be generated.
 Defaults to <code>true</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="enableDestinationReachedNotification">
<h3>enableDestinationReachedNotification</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enableDestinationReachedNotification</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.27.0. Use the <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#arrivalNotificationOption"><code>arrivalNotificationOption</code></a> instead</p></div>
</div>
<div className="block"><p>A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
 Defaults to <code>true</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="arrivalNotificationOption">
<h3>arrivalNotificationOption</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-arrivalnotificationoption" title="enum class in com.here.sdk.navigation">ArrivalNotificationOption</a></span> <span className="element-name">arrivalNotificationOption</span></div>
<div className="block"><p>A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated.
 Defaults to <code>ArrivalNotificationOption.BOTH</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="enableDoubleNotification">
<h3>enableDoubleNotification</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enableDoubleNotification</span></div>
<div className="block"><p>A flag that indicates whether combined maneuver notifications should be generated.
 Such double notifications can be useful when maneuvers are very close.
 <strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'.
 This way a user can better anticipate the next-next maneuver.
 Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
 When the next-next maneuver action takes place, the notification will be given as usual.
 <strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'.
 Defaults to <code>true</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="enablePhoneme">
<h3>enablePhoneme</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enablePhoneme</span></div>
<div className="block"><p>A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
 road numbers, city names) should be used when generating notifications. Direction information comes usually
 in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is
 synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
 and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
 direction information sound more natural.
 <strong>Note:</strong> For now, this property is functional for road name and road number information only.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="notificationFormatOption">
<h3>notificationFormatOption</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a></span> <span className="element-name">notificationFormatOption</span></div>
<div className="block"><p>A formatting option for the phoneme that is included in the notification. By default, no phoneme is used
 and the <a href="sdk-for-android-navigate-notificationformatoption#PLAIN"><code>NotificationFormatOption.PLAIN</code></a> orthographic form is included in the notification.
 <strong>Note:</strong>
 To use the SSML format for phonemes, <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enablePhoneme"><code>enablePhoneme</code></a> needs to be set to <code>true</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="textUsageOptions">
<h3>textUsageOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a></span> <span className="element-name">textUsageOptions</span></div>
<div className="block"><p>An option whether street name, road number and sign post direction should be used when generating notification.
 Defaults to each attribute as <a href="sdk-for-android-navigate-localizedtextpreference#USE_ALWAYS"><code>LocalizedTextPreference.USE_ALWAYS</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="enableHighwayExit">
<h3>enableHighwayExit</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enableHighwayExit</span></div>
<div className="block"><p>A flag that indicates whether highway exit information should be used when generating notification.
 Defaults to <code>true</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="enableLaneRecommendation">
<h3>enableLaneRecommendation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">enableLaneRecommendation</span></div>
<div className="block"><p>A flag that indicates whether lane recommendation should be used when generating notifications.
 In case the flag is enabled, <em>only</em> the notification for the <a href="sdk-for-android-navigate-maneuvernotificationtype#DISTANCE"><code>ManeuverNotificationType.DISTANCE</code></a>
 maneuver notification type will contain the lane recommendation. The lane recommandation will replace the
 direction information in the notification.
 <strong>Example:</strong> 'After 250 meters use the right two lanes and turn right.'.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="includedNaturalGuidanceTypes">
<h3>includedNaturalGuidanceTypes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-naturalguidancetype" title="enum class in com.here.sdk.navigation">NaturalGuidanceType</a>&gt;</span> <span className="element-name">includedNaturalGuidanceTypes</span></div>
<div className="block"><p>List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-naturalguidancetype" title="enum class in com.here.sdk.navigation"><code>NaturalGuidanceType</code></a> should be included in the notifications. Excluding
 all of them will disable natural guidance information in the notifications completely.
 By default, the list is empty and natural guidance is disabled.</p></div>
</section>
</li>
<li>
<section className="detail" id="directionInformationUsageForActionNotificationOption">
<h3>directionInformationUsageForActionNotificationOption</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-directioninformationusageoption" title="enum class in com.here.sdk.navigation">DirectionInformationUsageOption</a></span> <span className="element-name">directionInformationUsageForActionNotificationOption</span></div>
<div className="block"><p>An option whether direction information should be used when generating notification with
 <a href="sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a>. Defaults to <a href="sdk-for-android-navigate-directioninformationusageoption#NONE"><code>DirectionInformationUsageOption.NONE</code></a>.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>ManeuverNotificationOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ManeuverNotificationOptions</span>()</div>
<div className="block"><p>Creates a new instance of this class with default configurations.</p></div>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem)">
<h3>ManeuverNotificationOptions</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="element-name">ManeuverNotificationOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.23.0. Use the default constructor instead.</p></div>
</div>
<div className="block"><p>Creates a new instance of this class with specified language and unit system.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - <p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></dd>
<dd><code>unitSystem</code> - <p>Defines the measurement system used for distances. Defaults to metric.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,com.here.sdk.routing.TextUsageOptions,boolean)">
<h3>ManeuverNotificationOptions</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="element-name">ManeuverNotificationOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a> textUsageOptions,
 boolean enableHighwayExit)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.23.0. Use the default constructor instead.</p></div>
</div>
<div className="block"><p>Creates a new instance of this class with full specified configurations.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - <p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></dd>
<dd><code>unitSystem</code> - <p>Defines the measurement system used for distances. Defaults to metric.</p></dd>
<dd><code>includedNotificationTypes</code> - <p>List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated. Excluding all of
 them will disable the maneuver notifications completely.
 By default, all types are included.</p></dd>
<dd><code>enableRoundaboutNotification</code> - <p>A flag that indicates whether notification for roundabout-related maneuvers should be generated.
 Defaults to <code>true</code>.</p></dd>
<dd><code>enableDestinationReachedNotification</code> - <p>A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
 Defaults to <code>true</code>.</p></dd>
<dd><code>enableDoubleNotification</code> - <p>A flag that indicates whether combined maneuver notifications should be generated.
 Such double notifications can be useful when maneuvers are very close.
 <strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'.
 This way a user can better anticipate the next-next maneuver.
 Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
 When the next-next maneuver action takes place, the notification will be given as usual.
 <strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'.
 Defaults to <code>true</code>.</p></dd>
<dd><code>enablePhoneme</code> - <p>A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
 road numbers, city names) should be used when generating notifications. Direction information comes usually
 in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is
 synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
 and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
 direction information sound more natural.
 <strong>Note:</strong> For now, this property is functional for road name and road number information only.
 Defaults to <code>false</code>.</p></dd>
<dd><code>textUsageOptions</code> - <p>An option whether street name, road number and sign post direction should be used when generating notification.
 Defaults to each attribute as <a href="sdk-for-android-navigate-localizedtextpreference#USE_ALWAYS"><code>LocalizedTextPreference.USE_ALWAYS</code></a>.</p></dd>
<dd><code>enableHighwayExit</code> - <p>A flag that indicates whether highway exit information should be used when generating notification.
 Defaults to <code>true</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,boolean)">
<h3>ManeuverNotificationOptions</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="element-name">ManeuverNotificationOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 boolean enableHighwayExit)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.23.0. Use the default constructor instead.</p></div>
</div>
<div className="block"><p>Creates a new instance of this class with full specified configurations.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - <p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></dd>
<dd><code>unitSystem</code> - <p>Defines the measurement system used for distances. Defaults to metric.</p></dd>
<dd><code>includedNotificationTypes</code> - <p>List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated. Excluding all of
 them will disable the maneuver notifications completely.
 By default, all types are included.</p></dd>
<dd><code>enableRoundaboutNotification</code> - <p>A flag that indicates whether notification for roundabout-related maneuvers should be generated.
 Defaults to <code>true</code>.</p></dd>
<dd><code>enableDestinationReachedNotification</code> - <p>A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
 Defaults to <code>true</code>.</p></dd>
<dd><code>enableDoubleNotification</code> - <p>A flag that indicates whether combined maneuver notifications should be generated.
 Such double notifications can be useful when maneuvers are very close.
 <strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'.
 This way a user can better anticipate the next-next maneuver.
 Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
 When the next-next maneuver action takes place, the notification will be given as usual.
 <strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'.
 Defaults to <code>true</code>.</p></dd>
<dd><code>enablePhoneme</code> - <p>A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
 road numbers, city names) should be used when generating notifications. Direction information comes usually
 in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is
 synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
 and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
 direction information sound more natural.
 <strong>Note:</strong> For now, this property is functional for road name and road number information only.
 Defaults to <code>false</code>.</p></dd>
<dd><code>enableHighwayExit</code> - <p>A flag that indicates whether highway exit information should be used when generating notification.
 Defaults to <code>true</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,com.here.sdk.navigation.NotificationFormatOption,boolean)">
<h3>ManeuverNotificationOptions</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="element-name">ManeuverNotificationOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a> notificationFormatOption,
 boolean enableHighwayExit)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.23.0. Use the default constructor instead.</p></div>
</div>
<div className="block"><p>Creates a new instance of this class with full specified configurations.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - <p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></dd>
<dd><code>unitSystem</code> - <p>Defines the measurement system used for distances. Defaults to metric.</p></dd>
<dd><code>includedNotificationTypes</code> - <p>List of <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated. Excluding all of
 them will disable the maneuver notifications completely.
 By default, all types are included.</p></dd>
<dd><code>enableRoundaboutNotification</code> - <p>A flag that indicates whether notification for roundabout-related maneuvers should be generated.
 Defaults to <code>true</code>.</p></dd>
<dd><code>enableDestinationReachedNotification</code> - <p>A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
 Defaults to <code>true</code>.</p></dd>
<dd><code>enableDoubleNotification</code> - <p>A flag that indicates whether combined maneuver notifications should be generated.
 Such double notifications can be useful when maneuvers are very close.
 <strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'.
 This way a user can better anticipate the next-next maneuver.
 Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
 When the next-next maneuver action takes place, the notification will be given as usual.
 <strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'.
 Defaults to <code>true</code>.</p></dd>
<dd><code>enablePhoneme</code> - <p>A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
 road numbers, city names) should be used when generating notifications. Direction information comes usually
 in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is
 synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
 and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
 direction information sound more natural.
 <strong>Note:</strong> For now, this property is functional for road name and road number information only.
 Defaults to <code>false</code>.</p></dd>
<dd><code>notificationFormatOption</code> - <p>A formatting option for the phoneme that is included in the notification. By default, no phoneme is used
 and the <a href="sdk-for-android-navigate-notificationformatoption#PLAIN"><code>NotificationFormatOption.PLAIN</code></a> orthographic form is included in the notification.
 <strong>Note:</strong>
 To use the SSML format for phonemes, <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions#enablePhoneme"><code>enablePhoneme</code></a> needs to be set to <code>true</code>.</p></dd>
<dd><code>enableHighwayExit</code> - <p>A flag that indicates whether highway exit information should be used when generating notification.
 Defaults to <code>true</code>.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
