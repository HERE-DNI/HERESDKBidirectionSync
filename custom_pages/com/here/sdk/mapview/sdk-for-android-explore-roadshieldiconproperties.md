---
title: "RoadShieldIconProperties (API Reference)"
slug: "sdk-for-android-explore-roadshieldiconproperties"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoadShieldIconProperties.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li>Method</li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.RoadShieldIconProperties</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RoadShieldIconProperties</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Contains the information required to create a road shield image.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#countryCode">countryCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#routeNumberName">routeNumberName</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A string that is used to additionally determine the road shield's visual representation.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-core-routetype" title="enum class in com.here.sdk.core">RouteType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#routeType">routeType</a></code></div>
<div class="col-last even-row-color">
<div class="block">The type of route indicating the significance of the road in a range from 0 to 6.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#shieldText">shieldText</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The text of the road-shield.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#stateCode">stateCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">The state code for the road.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.RouteType,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">RoadShieldIconProperties</a><wbr/>(<a href="sdk-for-android-explore-core-routetype" title="enum class in com.here.sdk.core">RouteType</a> routeType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> countryCode,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateCode,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> routeNumberName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> shieldText)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="routeType">
<h3>routeType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-core-routetype" title="enum class in com.here.sdk.core">RouteType</a></span> <span class="element-name">routeType</span></div>
<div class="block"><p>The type of route indicating the significance of the road in a range from 0 to 6. A value of
 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.</p></div>
</section>
</li>
<li>
<section class="detail" id="countryCode">
<h3>countryCode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">countryCode</span></div>
<div class="block"><p>The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</p></div>
</section>
</li>
<li>
<section class="detail" id="stateCode">
<h3>stateCode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">stateCode</span></div>
<div class="block"><p>The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example
 the ones listed for US on this page https://en.wikipedia.org/wiki/ISO_3166-2:US.
 The code "AL" is for Alabama. Another example is the code for autonomous
 communities listed on https://en.wikipedia.org/wiki/ISO_3166-2:ES. Can be empty if
 not required for the particular country.</p></div>
</section>
</li>
<li>
<section class="detail" id="routeNumberName">
<h3>routeNumberName</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">routeNumberName</span></div>
<div class="block"><p>A string that is used to additionally determine the road shield's visual representation.
 In a routing context, the text can be taken from a <code>LocalizedRoadNumber</code>, which
 is available for each <code>Span</code> of a <code>Route</code> object.
 Typically, the string contains the number of a road, such as "E100". Internally, the text
 is parsed with a RegEx pattern and the results will be used along with other properties
 such as <code>routeType</code>, <code>countryCode</code> and <code>stateCode</code> to identify the visual representation
 of a road shield icon.
 </p><p>Note that the actual text which will be displayed on the road shield icon is set with
 <a href="#shieldText"><code>shieldText</code></a>. In order to determine the visuals of the icon, <code>countryCode</code>, <code>routeType</code>
 and eventually the <code>stateCode</code> is in most cases sufficient to determine the type of road
 shield. In this case an empty string should be passed.
 </p><p><strong>Note:</strong> Texts that contain a <code>CardinalDirection</code> are currently not supported and may lead
 to unexpected results. See <code>LocalizedRoadNumber</code> for more details, it provides texts with
 and without a cardinal direction.</p></div>
</section>
</li>
<li>
<section class="detail" id="shieldText">
<h3>shieldText</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">shieldText</span></div>
<div class="block"><p>The text of the road-shield. This is the text which is displayed on the road-shield
 in reality. It will be in the output road-shield icon.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.RouteType,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>RoadShieldIconProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoadShieldIconProperties</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-routetype" title="enum class in com.here.sdk.core">RouteType</a> routeType,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> countryCode,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateCode,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> routeNumberName,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> shieldText)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeType</code> - <p>The type of route indicating the significance of the road in a range from 0 to 6. A value of
 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.</p></dd>
<dd><code>countryCode</code> - <p>The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</p></dd>
<dd><code>stateCode</code> - <p>The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example
 the ones listed for US on this page https://en.wikipedia.org/wiki/ISO_3166-2:US.
 The code "AL" is for Alabama. Another example is the code for autonomous
 communities listed on https://en.wikipedia.org/wiki/ISO_3166-2:ES. Can be empty if
 not required for the particular country.</p></dd>
<dd><code>routeNumberName</code> - <p>A string that is used to additionally determine the road shield's visual representation.
 In a routing context, the text can be taken from a <code>LocalizedRoadNumber</code>, which
 is available for each <code>Span</code> of a <code>Route</code> object.
 Typically, the string contains the number of a road, such as "E100". Internally, the text
 is parsed with a RegEx pattern and the results will be used along with other properties
 such as <code>routeType</code>, <code>countryCode</code> and <code>stateCode</code> to identify the visual representation
 of a road shield icon.
 </p><p>Note that the actual text which will be displayed on the road shield icon is set with
 <a href="#shieldText"><code>shieldText</code></a>. In order to determine the visuals of the icon, <code>countryCode</code>, <code>routeType</code>
 and eventually the <code>stateCode</code> is in most cases sufficient to determine the type of road
 shield. In this case an empty string should be passed.
 </p><p><strong>Note:</strong> Texts that contain a <code>CardinalDirection</code> are currently not supported and may lead
 to unexpected results. See <code>LocalizedRoadNumber</code> for more details, it provides texts with
 and without a cardinal direction.</p></dd>
<dd><code>shieldText</code> - <p>The text of the road-shield. This is the text which is displayed on the road-shield
 in reality. It will be in the output road-shield icon.</p></dd>
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
</div>



</div>
`
}</HTMLBlock>
