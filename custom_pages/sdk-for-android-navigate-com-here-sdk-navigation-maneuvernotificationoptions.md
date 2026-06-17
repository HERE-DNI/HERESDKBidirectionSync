---
title: "ManeuverNotificationOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ManeuverNotificationOptions.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.ManeuverNotificationOptions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ManeuverNotificationOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A class containing all options to be used when generating maneuver notifications.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-arrivalnotificationoption" title="enum class in com.here.sdk.navigation">ArrivalNotificationOption</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalNotificationOption">arrivalNotificationOption</a></code></div>
<div class="col-last even-row-color">
<div class="block">A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated.</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-directioninformationusageoption" title="enum class in com.here.sdk.navigation">DirectionInformationUsageOption</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#directionInformationUsageForActionNotificationOption">directionInformationUsageForActionNotificationOption</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An option whether direction information should be used when generating notification with
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a>.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enableDestinationReachedNotification">enableDestinationReachedNotification</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enableDoubleNotification">enableDoubleNotification</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A flag that indicates whether combined maneuver notifications should be generated.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enableHighwayExit">enableHighwayExit</a></code></div>
<div class="col-last even-row-color">
<div class="block">A flag that indicates whether highway exit information should be used when generating notification.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enableLaneRecommendation">enableLaneRecommendation</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A flag that indicates whether lane recommendation should be used when generating notifications.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enablePhoneme">enablePhoneme</a></code></div>
<div class="col-last even-row-color">
<div class="block">A flag that indicates whether phonemes in selected notification format for proper nouns (e.g.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enableRoundaboutNotification">enableRoundaboutNotification</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A flag that indicates whether notification for roundabout-related maneuvers should be generated.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-naturalguidancetype" title="enum class in com.here.sdk.navigation">NaturalGuidanceType</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#includedNaturalGuidanceTypes">includedNaturalGuidanceTypes</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-naturalguidancetype" title="enum class in com.here.sdk.navigation"><code>NaturalGuidanceType</code></a> should be included in the notifications.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#includedNotificationTypes">includedNotificationTypes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated.</div>
</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#language">language</a></code></div>
<div class="col-last even-row-color">
<div class="block">The language in which the notifications will be generated.</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#notificationFormatOption">notificationFormatOption</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A formatting option for the phoneme that is included in the notification.</div>
</div>
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#textUsageOptions">textUsageOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">An option whether street name, road number and sign post direction should be used when generating notification.</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#unitSystem">unitSystem</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines the measurement system used for distances.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E()">ManeuverNotificationOptions</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class with default configurations.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem)">ManeuverNotificationOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.23.0.</div>
</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,boolean)">ManeuverNotificationOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 boolean enableHighwayExit)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.23.0.</div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,com.here.sdk.navigation.NotificationFormatOption,boolean)">ManeuverNotificationOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a> notificationFormatOption,
 boolean enableHighwayExit)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.23.0.</div>
</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,com.here.sdk.routing.TextUsageOptions,boolean)">ManeuverNotificationOptions</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a> textUsageOptions,
 boolean enableHighwayExit)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.23.0.</div>
</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="language">
<h3>language</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></span> <span class="element-name">language</span></div>
<div class="block"><p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></div>
</section>
</li>
<li>
<section class="detail" id="unitSystem">
<h3>unitSystem</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></span> <span class="element-name">unitSystem</span></div>
<div class="block"><p>Defines the measurement system used for distances. Defaults to metric.</p></div>
</section>
</li>
<li>
<section class="detail" id="includedNotificationTypes">
<h3>includedNotificationTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt;</span> <span class="element-name">includedNotificationTypes</span></div>
<div class="block"><p>List of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated. Excluding all of
 them will disable the maneuver notifications completely.
 By default, all types are included.</p></div>
</section>
</li>
<li>
<section class="detail" id="enableRoundaboutNotification">
<h3>enableRoundaboutNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableRoundaboutNotification</span></div>
<div class="block"><p>A flag that indicates whether notification for roundabout-related maneuvers should be generated.
 Defaults to <code>true</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="enableDestinationReachedNotification">
<h3>enableDestinationReachedNotification</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableDestinationReachedNotification</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.27.0. Use the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#arrivalNotificationOption"><code>arrivalNotificationOption</code></a> instead</p></div>
</div>
<div class="block"><p>A flag that indicates whether notification for destination/stopover reached maneuvers should be generated.
 Defaults to <code>true</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="arrivalNotificationOption">
<h3>arrivalNotificationOption</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-arrivalnotificationoption" title="enum class in com.here.sdk.navigation">ArrivalNotificationOption</a></span> <span class="element-name">arrivalNotificationOption</span></div>
<div class="block"><p>A flag that indicates whether notification for destination and/or stopover reached maneuvers should be generated.
 Defaults to <code>ArrivalNotificationOption.BOTH</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="enableDoubleNotification">
<h3>enableDoubleNotification</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableDoubleNotification</span></div>
<div class="block"><p>A flag that indicates whether combined maneuver notifications should be generated.
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
<section class="detail" id="enablePhoneme">
<h3>enablePhoneme</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enablePhoneme</span></div>
<div class="block"><p>A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
 road numbers, city names) should be used when generating notifications. Direction information comes usually
 in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is
 synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
 and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
 direction information sound more natural.
 <strong>Note:</strong> For now, this property is functional for road name and road number information only.
 </p><p>Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="notificationFormatOption">
<h3>notificationFormatOption</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a></span> <span class="element-name">notificationFormatOption</span></div>
<div class="block"><p>A formatting option for the phoneme that is included in the notification. By default, no phoneme is used
 and the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-notificationformatoption#PLAIN"><code>NotificationFormatOption.PLAIN</code></a> orthographic form is included in the notification.
 </p><p><strong>Note:</strong>
 To use the SSML format for phonemes, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enablePhoneme"><code>enablePhoneme</code></a> needs to be set to <code>true</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="textUsageOptions">
<h3>textUsageOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a></span> <span class="element-name">textUsageOptions</span></div>
<div class="block"><p>An option whether street name, road number and sign post direction should be used when generating notification.
 Defaults to each attribute as <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-localizedtextpreference#USE_ALWAYS"><code>LocalizedTextPreference.USE_ALWAYS</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="enableHighwayExit">
<h3>enableHighwayExit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableHighwayExit</span></div>
<div class="block"><p>A flag that indicates whether highway exit information should be used when generating notification.
 Defaults to <code>true</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="enableLaneRecommendation">
<h3>enableLaneRecommendation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableLaneRecommendation</span></div>
<div class="block"><p>A flag that indicates whether lane recommendation should be used when generating notifications.
 In case the flag is enabled, <em>only</em> the notification for the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype#DISTANCE"><code>ManeuverNotificationType.DISTANCE</code></a>
 maneuver notification type will contain the lane recommendation. The lane recommandation will replace the
 direction information in the notification.
 <strong>Example:</strong> 'After 250 meters use the right two lanes and turn right.'.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="includedNaturalGuidanceTypes">
<h3>includedNaturalGuidanceTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-naturalguidancetype" title="enum class in com.here.sdk.navigation">NaturalGuidanceType</a>&gt;</span> <span class="element-name">includedNaturalGuidanceTypes</span></div>
<div class="block"><p>List of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-naturalguidancetype" title="enum class in com.here.sdk.navigation"><code>NaturalGuidanceType</code></a> should be included in the notifications. Excluding
 all of them will disable natural guidance information in the notifications completely.
 </p><p>By default, the list is empty and natural guidance is disabled.</p></div>
</section>
</li>
<li>
<section class="detail" id="directionInformationUsageForActionNotificationOption">
<h3>directionInformationUsageForActionNotificationOption</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-directioninformationusageoption" title="enum class in com.here.sdk.navigation">DirectionInformationUsageOption</a></span> <span class="element-name">directionInformationUsageForActionNotificationOption</span></div>
<div class="block"><p>An option whether direction information should be used when generating notification with
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a>. Defaults to <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-directioninformationusageoption#NONE"><code>DirectionInformationUsageOption.NONE</code></a>.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ManeuverNotificationOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span>()</div>
<div class="block"><p>Creates a new instance of this class with default configurations.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem)">
<h3>ManeuverNotificationOptions</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.23.0. Use the default constructor instead.</p></div>
</div>
<div class="block"><p>Creates a new instance of this class with specified language and unit system.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - <p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></dd>
<dd><code>unitSystem</code> - <p>Defines the measurement system used for distances. Defaults to metric.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,com.here.sdk.routing.TextUsageOptions,boolean)">
<h3>ManeuverNotificationOptions</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a> textUsageOptions,
 boolean enableHighwayExit)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.23.0. Use the default constructor instead.</p></div>
</div>
<div class="block"><p>Creates a new instance of this class with full specified configurations.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - <p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></dd>
<dd><code>unitSystem</code> - <p>Defines the measurement system used for distances. Defaults to metric.</p></dd>
<dd><code>includedNotificationTypes</code> - <p>List of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated. Excluding all of
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
 </p><p>Defaults to <code>false</code>.</p></dd>
<dd><code>textUsageOptions</code> - <p>An option whether street name, road number and sign post direction should be used when generating notification.
 Defaults to each attribute as <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-localizedtextpreference#USE_ALWAYS"><code>LocalizedTextPreference.USE_ALWAYS</code></a>.</p></dd>
<dd><code>enableHighwayExit</code> - <p>A flag that indicates whether highway exit information should be used when generating notification.
 Defaults to <code>true</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,boolean)">
<h3>ManeuverNotificationOptions</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 boolean enableHighwayExit)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.23.0. Use the default constructor instead.</p></div>
</div>
<div class="block"><p>Creates a new instance of this class with full specified configurations.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - <p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></dd>
<dd><code>unitSystem</code> - <p>Defines the measurement system used for distances. Defaults to metric.</p></dd>
<dd><code>includedNotificationTypes</code> - <p>List of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated. Excluding all of
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
 </p><p>Defaults to <code>false</code>.</p></dd>
<dd><code>enableHighwayExit</code> - <p>A flag that indicates whether highway exit information should be used when generating notification.
 Defaults to <code>true</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.LanguageCode,com.here.sdk.core.UnitSystem,java.util.List,boolean,boolean,boolean,boolean,com.here.sdk.navigation.NotificationFormatOption,boolean)">
<h3>ManeuverNotificationOptions</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> language,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a> unitSystem,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation">ManeuverNotificationType</a>&gt; includedNotificationTypes,
 boolean enableRoundaboutNotification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
 boolean enableDestinationReachedNotification,
 boolean enableDoubleNotification,
 boolean enablePhoneme,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-notificationformatoption" title="enum class in com.here.sdk.navigation">NotificationFormatOption</a> notificationFormatOption,
 boolean enableHighwayExit)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.23.0. Use the default constructor instead.</p></div>
</div>
<div class="block"><p>Creates a new instance of this class with full specified configurations.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>language</code> - <p>The language in which the notifications will be generated. When the specified language
 is not supported, the default language is used, which is English (American).</p></dd>
<dd><code>unitSystem</code> - <p>Defines the measurement system used for distances. Defaults to metric.</p></dd>
<dd><code>includedNotificationTypes</code> - <p>List of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> for which notifications should be generated. Excluding all of
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
 </p><p>Defaults to <code>false</code>.</p></dd>
<dd><code>notificationFormatOption</code> - <p>A formatting option for the phoneme that is included in the notification. By default, no phoneme is used
 and the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-notificationformatoption#PLAIN"><code>NotificationFormatOption.PLAIN</code></a> orthographic form is included in the notification.
 </p><p><strong>Note:</strong>
 To use the SSML format for phonemes, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#enablePhoneme"><code>enablePhoneme</code></a> needs to be set to <code>true</code>.</p></dd>
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
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
