---
title: "Positioning"
slug: "sdk-for-ios-navigate-api-reference-positioning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/Positioning"></a>
<a title="Positioning  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="img/carat.png"/>
        Positioning  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Positioning</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18AuthenticationDataV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AuthenticationData"></a>
<a class="token" href="#/s:7heresdk18AuthenticationDataV">AuthenticationData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authentication data</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-authenticationdata">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AuthenticationData</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AuthenticationErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/AuthenticationError"></a>
<a class="token" href="#/s:7heresdk19AuthenticationErrorO">AuthenticationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authentication error</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-authenticationerror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">AuthenticationError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AuthenticationError</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18ConfirmationStatusO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ConfirmationStatus"></a>
<a class="token" href="#/s:7heresdk18ConfirmationStatusO">ConfirmationStatus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Confirmation action specific status codes.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-confirmationstatus">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ConfirmationStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LocationAccuracyO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LocationAccuracy"></a>
<a class="token" href="#/s:7heresdk16LocationAccuracyO">LocationAccuracy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the desired location accuracy, however the actual accuracy is not
guaranteed. When requesting high-accuracy locations, the initial update delivered
by the LocationEngine may not have the requested accuracy. Requesting higher
accuracy location updates usually means higher power consumption, therefore
you should use the lowest accuracy suitable for your use case to preserve the
device battery.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-locationaccuracy">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LocationAccuracy</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/LocationEngineBase"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP">LocationEngineBase</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Public protocol that describes the behaviour of <code><a href="sdk-for-ios-navigate-api-reference-classes-locationengine">LocationEngine</a></code>.
Implementation is platform-specific.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-locationenginebase">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">LocationEngineBase</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20LocationEngineStatusO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LocationEngineStatus"></a>
<a class="token" href="#/s:7heresdk20LocationEngineStatusO">LocationEngineStatus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the status of the LocationEngine.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-locationenginestatus">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LocationEngineStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationFeatureO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LocationFeature"></a>
<a class="token" href="#/s:7heresdk15LocationFeatureO">LocationFeature</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Location features supported by HERE positioning.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-locationfeature">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LocationFeature</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LocationEngine"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC">LocationEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class handles location updates received according to the desired LocationAccuracy.
Each instance of this class will be using internally the same client providing the actual
location updates. For that reason, only one LocationEngine can be started at a time.
Multiple delegates can be attached, either to receive location updates, see LocationUpdateDelegate,
or status updates, see LocationStatusDelegate. When a different LocationAccuracy is
desired, the LocationEngine needs to be stopped and started again.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-locationengine">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LocationEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-locationenginebase">LocationEngineBase</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationSimulatorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LocationSimulator"></a>
<a class="token" href="#/s:7heresdk17LocationSimulatorC">LocationSimulator</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Use the <code>LocationSimulator</code> to generate locations along a route or a GPX document. It notifies
the registered object about the current location at a fixed interval. In order to customize
the interval, see <code><a href="sdk-for-ios-navigate-api-reference-structs-locationsimulatoroptions">LocationSimulatorOptions</a></code>.
The locations are closely matched to the shape and proceeded from the start to the
destination as found in the provided route or the GPX document.
When providing a route, the <code>LocationSimulator</code> uses a base speed taken from each span
found in the provided route object. This base speed can be multiplied upfront
with a custom <code>speedFactor</code> for simulation purposes.
Effectively, this means that traffic-related information is not considered
to adjust the speed of the simulation.
For the <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></code>, a speed is either based on timestamps in the original file or provided by the user. The following data is read from a <code><a href="sdk-for-ios-navigate-api-reference-classes-gpxtrack">GPXTrack</a></code> and inserted into the provided <code><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></code> object: <code>latitude</code>, <code>longitude</code>, <code>altitude</code>, <code>time</code>, <code>bearingInDegrees</code>, <code>speedInMetersPerSecond</code>, <code>horizontalAccuracyInMeters</code>, <code>verticalAccuracyInMeters</code> and <code>locationTechnology</code>.</p>
<p>Note that simulation works offline and independent from any map data</p>
<ul>
<li>only the information found in the provided route or GPX document is considered.</li>
<li>When initializing the <code>LocationSimulator</code> with a route, then interpolations take place between the vertices of the route’s
polyline. The distance between interpolated locations is a function of the current span’s speed and the set notification interval.</li>
<li>When initializing the <code>LocationSimulator</code> with a GPX file, the <code>LocationSimulator</code> does not apply
any interpolation on the provided location data as this would shadow the recorded GPX data.</li>
</ul>
<p>Notifications will stop after the entire route has been traveled.</p>
<p><strong>Note:</strong>
Map-matched locations are only accessible from <code><a href="sdk-for-ios-navigate-api-reference-structs-routeprogress">RouteProgress</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-locationsimulator">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LocationSimulator</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationSimulator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationSimulator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24LocationSimulatorOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LocationSimulatorOptions"></a>
<a class="token" href="#/s:7heresdk24LocationSimulatorOptionsV">LocationSimulatorOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options to specify how the location simulator will behave.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-locationsimulatoroptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LocationSimulatorOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22LocationStatusDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/LocationStatusDelegate"></a>
<a class="token" href="#/s:7heresdk22LocationStatusDelegateP">LocationStatusDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Protocol for listening the
LocationEngine status updates.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-locationstatusdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">LocationStatusDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
}</HTMLBlock>
