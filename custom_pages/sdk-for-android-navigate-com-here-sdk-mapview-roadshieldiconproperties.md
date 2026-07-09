---
title: "RoadShieldIconProperties (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RoadShieldIconProperties.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.RoadShieldIconProperties</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RoadShieldIconProperties</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Contains the information required to create a road shield image.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties#countryCode">countryCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties#routeNumberName">routeNumberName</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A string that is used to additionally determine the road shield's visual representation.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-routetype" title="enum class in com.here.sdk.core">RouteType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties#routeType">routeType</a></code></div>
<div className="col-last even-row-color">
<div className="block">The type of route indicating the significance of the road in a range from 0 to 6.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties#shieldText">shieldText</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The text of the road-shield.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties#stateCode">stateCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">The state code for the road.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties#%3Cinit%3E(com.here.sdk.core.RouteType,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">RoadShieldIconProperties</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-routetype" title="enum class in com.here.sdk.core">RouteType</a> routeType,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> countryCode,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateCode,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> routeNumberName,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> shieldText)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="routeType">
<h3>routeType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-routetype" title="enum class in com.here.sdk.core">RouteType</a></span> <span className="element-name">routeType</span></div>
<div className="block"><p>The type of route indicating the significance of the road in a range from 0 to 6. A value of
 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.</p></div>
</section>
</li>
<li>
<section className="detail" id="countryCode">
<h3>countryCode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">countryCode</span></div>
<div className="block"><p>The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</p></div>
</section>
</li>
<li>
<section className="detail" id="stateCode">
<h3>stateCode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">stateCode</span></div>
<div className="block"><p>The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example
 the ones listed for US on this page https://en.wikipedia.org/wiki/ISO_3166-2:US.
 The code "AL" is for Alabama. Another example is the code for autonomous
 communities listed on https://en.wikipedia.org/wiki/ISO_3166-2:ES. Can be empty if
 not required for the particular country.</p></div>
</section>
</li>
<li>
<section className="detail" id="routeNumberName">
<h3>routeNumberName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">routeNumberName</span></div>
<div className="block"><p>A string that is used to additionally determine the road shield's visual representation.
 In a routing context, the text can be taken from a <code>LocalizedRoadNumber</code>, which
 is available for each <code>Span</code> of a <code>Route</code> object.
 Typically, the string contains the number of a road, such as "E100". Internally, the text
 is parsed with a RegEx pattern and the results will be used along with other properties
 such as <code>routeType</code>, <code>countryCode</code> and <code>stateCode</code> to identify the visual representation
 of a road shield icon.
 Note that the actual text which will be displayed on the road shield icon is set with
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties#shieldText"><code>shieldText</code></a>. In order to determine the visuals of the icon, <code>countryCode</code>, <code>routeType</code>
 and eventually the <code>stateCode</code> is in most cases sufficient to determine the type of road
 shield. In this case an empty string should be passed.
 <strong>Note:</strong> Texts that contain a <code>CardinalDirection</code> are currently not supported and may lead
 to unexpected results. See <code>LocalizedRoadNumber</code> for more details, it provides texts with
 and without a cardinal direction.</p></div>
</section>
</li>
<li>
<section className="detail" id="shieldText">
<h3>shieldText</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">shieldText</span></div>
<div className="block"><p>The text of the road-shield. This is the text which is displayed on the road-shield
 in reality. It will be in the output road-shield icon.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.RouteType,java.lang.String,java.lang.String,java.lang.String,java.lang.String)">
<h3>RoadShieldIconProperties</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RoadShieldIconProperties</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-routetype" title="enum class in com.here.sdk.core">RouteType</a> routeType,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> countryCode,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stateCode,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> routeNumberName,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> shieldText)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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
 Note that the actual text which will be displayed on the road shield icon is set with
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties#shieldText"><code>shieldText</code></a>. In order to determine the visuals of the icon, <code>countryCode</code>, <code>routeType</code>
 and eventually the <code>stateCode</code> is in most cases sufficient to determine the type of road
 shield. In this case an empty string should be passed.
 <strong>Note:</strong> Texts that contain a <code>CardinalDirection</code> are currently not supported and may lead
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

</div>
</div>



</div>
`
}</HTMLBlock>
