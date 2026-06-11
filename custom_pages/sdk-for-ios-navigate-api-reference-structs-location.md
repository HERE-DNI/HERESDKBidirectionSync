---
title: "Location"
slug: "sdk-for-ios-navigate-api-reference-structs-location"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Location"></a>
<a title="Location Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-core">Core</a>

        Location Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Location</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Location</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Describes a location in the world at a given time.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV16bearingInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bearingInDegrees"></a>
<a class="token" href="#/s:7heresdk8LocationV16bearingInDegreesSdSgvp">bearingInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bearing (also known as course) is the device’s horizontal direction of travel.
Starts at 0 in the geographical north and rotates around the compass in a clockwise
direction. This means for going north it is equal to 0, for northeast it is 45,
for east it is 90 and so on. Note that this may be different from the orientation of
the device. If it cannot be determined, the value is <code>nil</code>. Otherwise, it is
guaranteed to be in the range [0, 360).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">bearingInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV22speedInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk8LocationV22speedInMetersPerSecondSdSgvp">speedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Current speed of the device. If it cannot be determined, the value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV4time10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/time"></a>
<a class="token" href="#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">time</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time at which the location was determined.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">time</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/horizontalAccuracyInMeters"></a>
<a class="token" href="#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">horizontalAccuracyInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated horizontal accuracy. The actual location will lie within this radius of uncertainty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">horizontalAccuracyInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV24verticalAccuracyInMetersSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/verticalAccuracyInMeters"></a>
<a class="token" href="#/s:7heresdk8LocationV24verticalAccuracyInMetersSdSgvp">verticalAccuracyInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimated vertical accuracy.
Given that the received Location contains the altitude, the real value of the altitude
is estimated to lie within the following range:
[altitude - vertical accuracy, altitude + vertical accuracy].
For example, when the altitude is equal to 50 and the vertical accuracy
is 8, then the actual value is most likely in the range [42, 58].</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">verticalAccuracyInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV24bearingAccuracyInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bearingAccuracyInDegrees"></a>
<a class="token" href="#/s:7heresdk8LocationV24bearingAccuracyInDegreesSdSgvp">bearingAccuracyInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimated bearing accuracy for this location, in degrees.
If it cannot be determined, the value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">bearingAccuracyInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV30speedAccuracyInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedAccuracyInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk8LocationV30speedAccuracyInMetersPerSecondSdSgvp">speedAccuracyInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimated speed accuracy of this location, in meters per second.
If it cannot be determined, the value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedAccuracyInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV18timestampSinceBootSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timestampSinceBoot"></a>
<a class="token" href="#/s:7heresdk8LocationV18timestampSinceBootSdSgvp">timestampSinceBoot</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time at which the location was determined, relative to device
boot time. This time is monotonic and not affected by leap time or other system
time adjustments, so this is the recommended basis for general purpose interval timing
between location updates.
If it cannot be determined, the value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timestampSinceBoot</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV18locationTechnologyAA0bD0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/locationTechnology"></a>
<a class="token" href="#/s:7heresdk8LocationV18locationTechnologyAA0bD0OSgvp">locationTechnology</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional technology or provider of this location.
If it cannot be determined, the value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">locationTechnology</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationtechnology">LocationTechnology</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV6sourceAA0B6SourceOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/source"></a>
<a class="token" href="#/s:7heresdk8LocationV6sourceAA0B6SourceOSgvp">source</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional source of this location.
If it cannot be determined, the value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">source</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationsource">LocationSource</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV8gnssTimeSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/gnssTime"></a>
<a class="token" href="#/s:7heresdk8LocationV8gnssTimeSdSgvp">gnssTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional gnss time at which the location was determined.
It is a time interval from the Unix time epoch in milliseconds.
If it cannot be determined, the value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">gnssTime</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV14pitchInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pitchInDegrees"></a>
<a class="token" href="#/s:7heresdk8LocationV14pitchInDegreesSdSgvp">pitchInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pitch of this location, in degrees.
If it cannot be determined, the value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pitchInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LocationV11coordinates16bearingInDegrees05speedE15MetersPerSecond4time018horizontalAccuracyeH008verticalmeH00dmeF00gmehiJ018timestampSinceBoot18locationTechnology6source8gnssTime05pitcheF0AcA14GeoCoordinatesV_SdSgAS10Foundation4DateVSgA5sA0bS0OSgAA0B6SourceOSgA2Stcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(coordinates:bearingInDegrees:speedInMetersPerSecond:time:horizontalAccuracyInMeters:verticalAccuracyInMeters:bearingAccuracyInDegrees:speedAccuracyInMetersPerSecond:timestampSinceBoot:locationTechnology:source:gnssTime:pitchInDegrees:)"></a>
<a class="token" href="#/s:7heresdk8LocationV11coordinates16bearingInDegrees05speedE15MetersPerSecond4time018horizontalAccuracyeH008verticalmeH00dmeF00gmehiJ018timestampSinceBoot18locationTechnology6source8gnssTime05pitcheF0AcA14GeoCoordinatesV_SdSgAS10Foundation4DateVSgA5sA0bS0OSgAA0B6SourceOSgA2Stcfc">init(coordinates:<wbr/>bearingInDegrees:<wbr/>speedInMetersPerSecond:<wbr/>time:<wbr/>horizontalAccuracyInMeters:<wbr/>verticalAccuracyInMeters:<wbr/>bearingAccuracyInDegrees:<wbr/>speedAccuracyInMetersPerSecond:<wbr/>timestampSinceBoot:<wbr/>locationTechnology:<wbr/>source:<wbr/>gnssTime:<wbr/>pitchInDegrees:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of the class with specified parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">bearingInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">speedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">time</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">horizontalAccuracyInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">verticalAccuracyInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">bearingAccuracyInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">speedAccuracyInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">timestampSinceBoot</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">locationTechnology</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationtechnology">LocationTechnology</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">source</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationsource">LocationSource</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">gnssTime</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">pitchInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
