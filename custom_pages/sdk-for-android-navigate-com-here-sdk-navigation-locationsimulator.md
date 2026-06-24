---
title: "LocationSimulator (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationSimulator.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.LocationSimulator</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LocationSimulator</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Use the <code>LocationSimulator</code> to generate locations along a route or a GPX document. It notifies
 the registered object about the current location at a fixed interval. In order to customize
 the interval, see <a href="sdk-for-android-navigate-locationsimulatoroptions" title="class in com.here.sdk.navigation"><code>LocationSimulatorOptions</code></a>.
 The locations are closely matched to the shape and proceeded from the start to the
 destination as found in the provided route or the GPX document.
 When providing a route, the <code>LocationSimulator</code> uses a base speed taken from each span
 found in the provided route object. This base speed can be multiplied upfront
 with a custom <code>speedFactor</code> for simulation purposes.
 Effectively, this means that traffic-related information is not considered
 to adjust the speed of the simulation.
 For the <code>GPXTrack</code>, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a <code>GPXTrack</code> and inserted into the provided <code>Location</code> object: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code> and <code>locationTechnology</code>.
 </p><p>Note that simulation works offline and independent from any map data
 <ul>
<li>only the information found in the provided route or GPX document is considered.</li>
<li>When initializing the <code>LocationSimulator</code> with a route, then interpolations take place between the vertices of the route's
 polyline. The distance between interpolated locations is a function of the current span's speed and the set notification interval.</li>
<li>When initializing the <code>LocationSimulator</code> with a GPX file, the <code>LocationSimulator</code> does not apply
 any interpolation on the provided location data as this would shadow the recorded GPX data.</li>
</ul>
</p><p>Notifications will stop after the entire route has been traveled.
 </p><p><strong>Note:</strong>
 Map-matched locations are only accessible from <a href="sdk-for-android-navigate-routeprogress" title="class in com.here.sdk.navigation"><code>RouteProgress</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator#%3Cinit%3E(com.here.sdk.navigation.GPXTrack,com.here.sdk.navigation.LocationSimulatorOptions)">LocationSimulator</a><wbr/>(<a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> gpxTrack,
 <a href="sdk-for-android-navigate-locationsimulatoroptions" title="class in com.here.sdk.navigation">LocationSimulatorOptions</a> options)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a location simulator</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator#%3Cinit%3E(com.here.sdk.routing.Route,com.here.sdk.navigation.LocationSimulatorOptions)">LocationSimulator</a><wbr/>(<a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> route,
 <a href="sdk-for-android-navigate-locationsimulatoroptions" title="class in com.here.sdk.navigation">LocationSimulatorOptions</a> options)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator#getListener()">getListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a <code>LocationListener</code> that notifies on location updates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator#pause()">pause</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Pauses sending notifications to the subscribers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator#resume()">resume</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Resumes sending notifications to the subscribers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator#setListener(com.here.sdk.core.LocationListener)">setListener</a><wbr/>(<a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a <code>LocationListener</code> that notifies on location updates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator#start()">start</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts the location provider to send notifications to the subscribers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-locationsimulator#stop()">stop</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Stops the location provider from sending notifications to the subscribers.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.Route,com.here.sdk.navigation.LocationSimulatorOptions)">
<h3>LocationSimulator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LocationSimulator</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> route,
 @NonNull
 <a href="sdk-for-android-navigate-locationsimulatoroptions" title="class in com.here.sdk.navigation">LocationSimulatorOptions</a> options)</span>
                  throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>route</code> - <p>The route to travel.</p></dd>
<dd><code>options</code> - <p>The options to specify how the location simulator will behave.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.navigation.GPXTrack,com.here.sdk.navigation.LocationSimulatorOptions)">
<h3>LocationSimulator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LocationSimulator</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> gpxTrack,
 @NonNull
 <a href="sdk-for-android-navigate-locationsimulatoroptions" title="class in com.here.sdk.navigation">LocationSimulatorOptions</a> options)</span>
                  throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Create a location simulator</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>gpxTrack</code> - <p>The GPX track to travel.</p></dd>
<dd><code>options</code> - <p>The options to specify how the location simulator will behave.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section class="detail" id="start()">
<h3>start</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span>()</div>
<div class="block"><p>Starts the location provider to send notifications to the subscribers.
 Calling this method will always start the location simulator from the route's first
 <a href="sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a>, even if a simulation has already been started or stopped.</p></div>
</section>
</li>
<li>
<section class="detail" id="stop()">
<h3>stop</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stop</span>()</div>
<div class="block"><p>Stops the location provider from sending notifications to the subscribers.</p></div>
</section>
</li>
<li>
<section class="detail" id="pause()">
<h3>pause</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">pause</span>()</div>
<div class="block"><p>Pauses sending notifications to the subscribers.
 Calling this function has no effect when location provider is not started.</p></div>
</section>
</li>
<li>
<section class="detail" id="resume()">
<h3>resume</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">resume</span>()</div>
<div class="block"><p>Resumes sending notifications to the subscribers.
 Calling this function has no effect when location provider is not started.</p></div>
</section>
</li>
<li>
<section class="detail" id="getListener()">
<h3>getListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span> <span class="element-name">getListener</span>()</div>
<div class="block"><p>Gets a <code>LocationListener</code> that notifies on location updates.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The object that notifies on location updates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setListener(com.here.sdk.core.LocationListener)">
<h3>setListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> value)</span></div>
<div class="block"><p>Sets a <code>LocationListener</code> that notifies on location updates.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The object that notifies on location updates.</p></dd>
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
