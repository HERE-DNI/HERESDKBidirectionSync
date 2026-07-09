---
title: "MapSceneLights (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapSceneLights.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapSceneLights</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapSceneLights</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Manage the lights and their attributes in a scene.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a></code></div>
<div className="col-last even-row-color">
<div className="block">This callback function allows handling errors that occur during the setting of light attributes.</div>
</div>
<div className="col-first odd-row-color"><code>static enum </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingerror" title="enum class in com.here.sdk.mapview">MapSceneLights.AttributeSettingError</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Error enum indicating reasons for failure when setting light attributes.</div>
</div>
<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a></code></div>
<div className="col-last even-row-color">
<div className="block">The scene uses three categories of lighting which are:
 Main light, Back light and Rim light.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction" title="class in com.here.sdk.mapview">MapSceneLights.Direction</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The direction of lights as a pair of azimuth and altitude angles.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="setColor(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.core.Color,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)">
<h3>setColor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setColor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a> callback)</span></div>
<div className="block"><p>Set a new color for the light based on its category.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light for which the color is set.</p></dd>
<dd><code>color</code> - <p>The Color type includes red, green, blue, and alpha components.
     The value of these components must be inside the range [0, 1].</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setIntensity(com.here.sdk.mapview.MapSceneLights.Category,double,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)">
<h3>setIntensity</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setIntensity</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category,
 double intensity,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a> callback)</span></div>
<div className="block"><p>Set a new intensity for the light based on its category.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light for which the intensity is set.</p></dd>
<dd><code>intensity</code> - <p>The light intensity value must be inside the range [0, 10].
     The intensity value is clamped to this range.
     If the value falls outside its supported range, it will be adjusted to stay within the range.
     Note: When the intensity value is big,
     3D objects might turn completely white because all the color channels could go over the limit of 1.0.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDirection(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.mapview.MapSceneLights.Direction,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)">
<h3>setDirection</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDirection</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction" title="class in com.here.sdk.mapview">MapSceneLights.Direction</a> direction,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a> callback)</span></div>
<div className="block"><p>Set a new direction for the light based on its category.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light for which the direction is set.</p></dd>
<dd><code>direction</code> - <p>The Direction contains azimuth and altitude angles in degrees.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getColor(com.here.sdk.mapview.MapSceneLights.Category)">
<h3>getColor</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getColor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category)</span></div>
<div className="block"><p>Retrieves the current color of the light based on its category.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light from which the color is retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The current color of the light, or <code>null</code> if the light is missing from the loaded scene
     or MapScene is not intitialized.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getIntensity(com.here.sdk.mapview.MapSceneLights.Category)">
<h3>getIntensity</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getIntensity</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category)</span></div>
<div className="block"><p>Retrieves the current intensity of the light based on its category.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light from which the intensity is retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The current intensity of the light, or <code>null</code> if the light is missing from the loaded scene
     or MapScene is not intitialized.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDirection(com.here.sdk.mapview.MapSceneLights.Category)">
<h3>getDirection</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction" title="class in com.here.sdk.mapview">MapSceneLights.Direction</a></span> <span className="element-name">getDirection</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category)</span></div>
<div className="block"><p>Retrieves the current direction of the light based on its category.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light from which the direction is retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The current direction of the light, or <code>null</code> if the light is missing from the loaded scene
     or MapScene is not intitialized.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="reset()">
<h3>reset</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">reset</span>()</div>
<div className="block"><p>Resets all attributes of each light to their default values based on the current map scene settings.</p></div>
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
