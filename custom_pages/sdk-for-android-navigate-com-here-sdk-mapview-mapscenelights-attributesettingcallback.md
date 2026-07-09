---
title: "MapSceneLights.AttributeSettingCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapSceneLights.AttributeSettingCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights" title="class in com.here.sdk.mapview">MapSceneLights</a></dd>
</dl>
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public static interface </span><span className="element-name type-name-label">MapSceneLights.AttributeSettingCallback</span></div>
<div className="block"><p>This callback function allows handling errors that occur during the setting of light attributes.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="onAttributeSetting(com.here.sdk.mapview.MapSceneLights.AttributeSettingError)">
<h3>onAttributeSetting</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onAttributeSetting</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingerror" title="enum class in com.here.sdk.mapview">MapSceneLights.AttributeSettingError</a> setLightError)</span></div>
<div className="block"><p>This callback function allows handling errors that occur during the setting of light attributes.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>setLightError</code> - <p>The cause for the failure when setting the light attributes, or <code>null</code> if no error occurred.
     Note: The error code <code>NO_LIGHTS</code> may be returned when attempting to set light attributes in map schemes
     that do not support lights, for instance <code>road.network</code> map scheme.
     Please refer to the error code documentation for further details on error handling.</p></dd>
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
