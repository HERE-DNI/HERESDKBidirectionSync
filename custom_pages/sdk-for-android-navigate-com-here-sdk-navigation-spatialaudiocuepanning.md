---
title: "SpatialAudioCuePanning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SpatialAudioCuePanning.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.SpatialAudioCuePanning</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SpatialAudioCuePanning</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Use the <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation"><code>SpatialAudioCuePanning</code></a> to notify each of the azimuths which compose a spatial audio
 trajectory along the audio cue.</p></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning.spatialazimuthcallback" title="interface in com.here.sdk.navigation">SpatialAudioCuePanning.SpatialAzimuthCallback</a></code></div>
<div class="col-last even-row-color">
<div class="block">Called once <code>startAngularPanning()</code> starts.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning#startAngularPanning(com.here.sdk.navigation.CustomPanningData,com.here.sdk.navigation.SpatialAudioCuePanning.SpatialAzimuthCallback)">startAngularPanning</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata" title="class in com.here.sdk.navigation">CustomPanningData</a> nextCustomPanningData,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning.spatialazimuthcallback" title="interface in com.here.sdk.navigation">SpatialAudioCuePanning.SpatialAzimuthCallback</a> azimuthCallback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer.</div>
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
<section class="detail" id="startAngularPanning(com.here.sdk.navigation.CustomPanningData,com.here.sdk.navigation.SpatialAudioCuePanning.SpatialAzimuthCallback)">
<h3>startAngularPanning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startAngularPanning</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata" title="class in com.here.sdk.navigation">CustomPanningData</a> nextCustomPanningData,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning.spatialazimuthcallback" title="interface in com.here.sdk.navigation">SpatialAudioCuePanning.SpatialAzimuthCallback</a> azimuthCallback)</span></div>
<div class="block"><p>This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer.
 An optional custom value for <a href="sdk-for-android-navigate-custompanningdata#estimatedAudioCueDuration"><code>CustomPanningData.estimatedAudioCueDuration</code></a>,
 <a href="sdk-for-android-navigate-custompanningdata#initialAzimuthInDegrees"><code>CustomPanningData.initialAzimuthInDegrees</code></a>,  or its <a href="sdk-for-android-navigate-custompanningdata#sweepAzimuthInDegrees"><code>CustomPanningData.sweepAzimuthInDegrees</code></a>
 can be here defined if the default data does not fully match the utilized Language or TTS engine
 or angle expectations.
 If startAngularPanning is called to spatialize the audio cue of a new maneuver before the full
 completion of a previous spatial audio trajectory, then <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation"><code>EventTextListener</code></a> will retrieve
 the azimuth values of the new maneuver.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>nextCustomPanningData</code> - <p>Defines a new set of values related to spatial audio panning.
     When <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata" title="class in com.here.sdk.navigation"><code>CustomPanningData</code></a> is initialized as <code>null</code>, the default set of values provided by HERE SDK
     will be used instead.</p></dd>
<dd><code>azimuthCallback</code> - <p>Callback that will signal the next azimuth required to complete a spatial audio trajectory
     once the angular panning has started.
     Azimuth angular values are retrieved individually until the full duration of the audio trajectory
     has been reached,
     or a new text message has started its angular panning.</p></dd>
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
`
}</HTMLBlock>
