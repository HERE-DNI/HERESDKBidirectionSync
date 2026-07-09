---
title: "SpatialAudioCuePanning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SpatialAudioCuePanning.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.SpatialAudioCuePanning</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SpatialAudioCuePanning</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Use the <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning" title="class in com.here.sdk.navigation"><code>SpatialAudioCuePanning</code></a> to notify each of the azimuths which compose a spatial audio
 trajectory along the audio cue.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning-spatialazimuthcallback" title="interface in com.here.sdk.navigation">SpatialAudioCuePanning.SpatialAzimuthCallback</a></code></div>
<div className="col-last even-row-color">
<div className="block">Called once <code>startAngularPanning()</code> starts.</div>
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
<section className="detail" id="startAngularPanning(com.here.sdk.navigation.CustomPanningData,com.here.sdk.navigation.SpatialAudioCuePanning.SpatialAzimuthCallback)">
<h3>startAngularPanning</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">startAngularPanning</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-custompanningdata" title="class in com.here.sdk.navigation">CustomPanningData</a> nextCustomPanningData,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialaudiocuepanning-spatialazimuthcallback" title="interface in com.here.sdk.navigation">SpatialAudioCuePanning.SpatialAzimuthCallback</a> azimuthCallback)</span></div>
<div className="block"><p>This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer.
 An optional custom value for <a href="sdk-for-android-navigate-custompanningdata#estimatedAudioCueDuration"><code>CustomPanningData.estimatedAudioCueDuration</code></a>,
 <a href="sdk-for-android-navigate-custompanningdata#initialAzimuthInDegrees"><code>CustomPanningData.initialAzimuthInDegrees</code></a>,  or its <a href="sdk-for-android-navigate-custompanningdata#sweepAzimuthInDegrees"><code>CustomPanningData.sweepAzimuthInDegrees</code></a>
 can be here defined if the default data does not fully match the utilized Language or TTS engine
 or angle expectations.
 If startAngularPanning is called to spatialize the audio cue of a new maneuver before the full
 completion of a previous spatial audio trajectory, then <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation"><code>EventTextListener</code></a> will retrieve
 the azimuth values of the new maneuver.</p></div>
<dl className="notes">
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
</div>



</div>
`
}</HTMLBlock>
