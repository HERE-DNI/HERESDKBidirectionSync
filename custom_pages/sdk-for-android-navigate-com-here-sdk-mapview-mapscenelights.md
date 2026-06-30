---
title: "MapSceneLights (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapSceneLights.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapSceneLights</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapSceneLights</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Manage the lights and their attributes in a scene.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a></code></div>
<div class="col-last even-row-color">
<div class="block">This callback function allows handling errors that occur during the setting of light attributes.</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingerror" title="enum class in com.here.sdk.mapview">MapSceneLights.AttributeSettingError</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Error enum indicating reasons for failure when setting light attributes.</div>
</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a></code></div>
<div class="col-last even-row-color">
<div class="block">The scene uses three categories of lighting which are:
 Main light, Back light and Rim light.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction" title="class in com.here.sdk.mapview">MapSceneLights.Direction</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The direction of lights as a pair of azimuth and altitude angles.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights#getColor(com.here.sdk.mapview.MapSceneLights.Category)">getColor</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves the current color of the light based on its category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction" title="class in com.here.sdk.mapview">MapSceneLights.Direction</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights#getDirection(com.here.sdk.mapview.MapSceneLights.Category)">getDirection</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves the current direction of the light based on its category.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights#getIntensity(com.here.sdk.mapview.MapSceneLights.Category)">getIntensity</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Retrieves the current intensity of the light based on its category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights#reset()">reset</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resets all attributes of each light to their default values based on the current map scene settings.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights#setColor(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.core.Color,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)">setColor</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a new color for the light based on its category.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights#setDirection(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.mapview.MapSceneLights.Direction,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)">setDirection</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction" title="class in com.here.sdk.mapview">MapSceneLights.Direction</a> direction,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a new direction for the light based on its category.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights#setIntensity(com.here.sdk.mapview.MapSceneLights.Category,double,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)">setIntensity</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category,
 double intensity,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set a new intensity for the light based on its category.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="setColor(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.core.Color,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)">
<h3>setColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a> callback)</span></div>
<div class="block"><p>Set a new color for the light based on its category.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light for which the color is set.</p></dd>
<dd><code>color</code> - <p>The Color type includes red, green, blue, and alpha components.
     The value of these components must be inside the range [0, 1].</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIntensity(com.here.sdk.mapview.MapSceneLights.Category,double,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)">
<h3>setIntensity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIntensity</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category,
 double intensity,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a> callback)</span></div>
<div class="block"><p>Set a new intensity for the light based on its category.</p></div>
<dl class="notes">
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
<section class="detail" id="setDirection(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.mapview.MapSceneLights.Direction,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)">
<h3>setDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirection</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction" title="class in com.here.sdk.mapview">MapSceneLights.Direction</a> direction,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-attributesettingcallback" title="interface in com.here.sdk.mapview">MapSceneLights.AttributeSettingCallback</a> callback)</span></div>
<div class="block"><p>Set a new direction for the light based on its category.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light for which the direction is set.</p></dd>
<dd><code>direction</code> - <p>The Direction contains azimuth and altitude angles in degrees.</p></dd>
<dd><code>callback</code> - <p>Optional callback that will receive the result of this operation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getColor(com.here.sdk.mapview.MapSceneLights.Category)">
<h3>getColor</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getColor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category)</span></div>
<div class="block"><p>Retrieves the current color of the light based on its category.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light from which the color is retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The current color of the light, or <code>null</code> if the light is missing from the loaded scene
     or MapScene is not intitialized.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntensity(com.here.sdk.mapview.MapSceneLights.Category)">
<h3>getIntensity</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getIntensity</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category)</span></div>
<div class="block"><p>Retrieves the current intensity of the light based on its category.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light from which the intensity is retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The current intensity of the light, or <code>null</code> if the light is missing from the loaded scene
     or MapScene is not intitialized.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDirection(com.here.sdk.mapview.MapSceneLights.Category)">
<h3>getDirection</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction" title="class in com.here.sdk.mapview">MapSceneLights.Direction</a></span> <span class="element-name">getDirection</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-category" title="enum class in com.here.sdk.mapview">MapSceneLights.Category</a> category)</span></div>
<div class="block"><p>Retrieves the current direction of the light based on its category.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - <p>The category of light from which the direction is retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The current direction of the light, or <code>null</code> if the light is missing from the loaded scene
     or MapScene is not intitialized.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="reset()">
<h3>reset</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reset</span>()</div>
<div class="block"><p>Resets all attributes of each light to their default values based on the current map scene settings.</p></div>
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
