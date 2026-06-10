---
title: "sdk-for-ios-explore-api-reference-classes-locationindicator"
slug: "sdk-for-ios-explore-api-reference-classes-locationindicator"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/LocationIndicator"></a>
<a title="LocationIndicator Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LocationIndicator Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationIndicator</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LocationIndicator</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationIndicator</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationIndicator</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Graphical object to represent the location of the user on the map.</p>
<p>It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style.
This style can be changed by <code><a href="../Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC08locationC5StyleAC0cE0Ovp">LocationIndicator.locationIndicatorStyle</a></code></p>
<p>The location is made available to an instance of this class by calling <code>LocationIndicator.updateLocation(Location)</code> or
<code>LocationIndicator.updateLocation(Location, MapCameraUpdate)</code>.</p>
<p>Use <code><a href="../Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC6enable3foryAA11MapViewBase_p_tF">LocationIndicator.enable(...)</a></code> to add this object to the map and <code><a href="../Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC7disableyyF">LocationIndicator.disable(...)</a></code> to remove it.</p>
<p>Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera
to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the
MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly
disappear from the viewport due to the new perspective.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of LocationIndicator.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC3forAcA11MapViewBase_p_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(for:)"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC3forAcA11MapViewBase_p_tcfc">init(for:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of LocationIndicator and adds it to provided <code><a href="sdk-for-ios-explore-api-reference-..-protocols-mapviewbase">MapViewBase</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="k">for</span> <span class="nv">mapView</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-mapviewbase">MapViewBase</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapView</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-explore-api-reference-..-protocols-mapviewbase">MapViewBase</a></code> instance.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC20isAccuracyVisualizedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isAccuracyVisualized"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC20isAccuracyVisualizedSbvp">isAccuracyVisualized</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.
By default, it is set to <code>false</code>. In this case the accuracy indicator halo
has a fixed and zoom level independent size. When set to
<code>true</code>, the radius of the halo corresponds to the value of
<code><a href="../Structs/Location.html#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">Location.horizontalAccuracyInMeters</a></code> passed to <code>LocationIndicator.updateLocation(Location)</code>
and scales in world coordinates.</p>
<p>For values smaller than 20 meters the halo is hidden.
The radius of the halo is limited to 500 meters and values higher than that or <code>nil</code>
will keep the halo at that size.</p>
<p>If the location indicator is set to inactive (which can be checked via <code><a href="../Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC8isActiveSbvp">LocationIndicator.isActive</a></code> flag),
then the halo is always hidden. The value of this property remains unchanged regardless of the flag’s value.
If the location indicator is set to active:</p>
<ul>
<li>Built-in location indicators:

<ul>
<li>The halo is always shown.</li>
<li>If the accuracy visualization is set to <code>true</code>, the size of the halo scales with
<code><a href="../Structs/Location.html#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">Location.horizontalAccuracyInMeters</a></code> in world coordinates.</li>
<li>If the accuracy visualization is set to <code>false</code>, halo displays at a default size.</li>
</ul></li>
<li>Custom location indicator:

<ul>
<li>If the accuracy visualization is set to <code>true</code>, halo is shown and the size of the halo scales with
<code><a href="../Structs/Location.html#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">Location.horizontalAccuracyInMeters</a></code> in world coordinates.</li>
<li>If the accuracy visualization is set to <code>false</code>, no halo is shown since it might not fit together with the custom 3d model.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isAccuracyVisualized</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC08locationC5StyleAC0cE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/locationIndicatorStyle"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC08locationC5StyleAC0cE0Ovp">locationIndicatorStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The visual style of location indicator.
By default, it is set to <code><a href="../Classes/LocationIndicator/IndicatorStyle.html#/s:7heresdk17LocationIndicatorC0C5StyleO10navigationyA2EmF">LocationIndicator.IndicatorStyle.navigation</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">locationIndicatorStyle</span><span class="p">:</span> <span class="kt">LocationIndicator</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-locationindicator-indicatorstyle">IndicatorStyle</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC8isActiveSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isActive"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC8isActiveSbvp">isActive</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A Boolean value that determines whether the active on inactive version of location indicator is shown.
By default, it is set to <code>true</code>.</p>
<p>Set to <code>false</code> to show the inactive version of the indicator which
is typically represented by a grayed out version of the indicator. This can be used in case
the location of the indicator might be outdated or positioning on the device is disabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isActive</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC7opacitySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/opacity"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC7opacitySdvp">opacity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The factor applied to the alpha channel of both the location indicator’s texture and the accuracy indicator’s halo color.
The value is clamped in range [0.0, 1.0]. Default value is 1.0 which means location
indicator is displayed with the default alpha channel of the texture.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">opacity</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC20materialReflectivityAA08MaterialE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/materialReflectivity"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC20materialReflectivityAA08MaterialE0VSgvp">materialReflectivity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The material reflectivity properties of the location indicator.
Enables per‑pixel lighting for all internal markers (navigation, pedestrian,
inactive variants) and the halo when assigned. While <code>materialReflectivity</code> is non‑null the
markers are shaded by scene lights using the provided ambient / diffuse factors. When set
back to <code>nil</code>, lighting is disabled and markers revert to unlit (emissive) rendering.
This value also applies to any custom markers set with <code>setMarker3dModel</code>.
Default value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">materialReflectivity</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-materialreflectivity">MaterialReflectivity</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC0C5StyleO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/IndicatorStyle"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC0C5StyleO">IndicatorStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The predefined styles for the location indicator which are pedestrian and navigation mode.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-locationindicator-indicatorstyle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">IndicatorStyle</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC10MarkerTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MarkerType"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC10MarkerTypeO">MarkerType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enum to identify different types of markers of the location indicator.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-locationindicator-markertype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MarkerType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC6enable3foryAA11MapViewBase_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/enable(for:)"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC6enable3foryAA11MapViewBase_p_tF">enable(for:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables <code>LocationIndicator</code> for provided <code><a href="sdk-for-ios-explore-api-reference-..-protocols-mapviewbase">MapViewBase</a></code>.
If <code>LocationIndicator</code> is already enabled (added to map view) for passed map view, this function does nothing.
If <code>LocationIndicator</code> is added to different <code><a href="sdk-for-ios-explore-api-reference-..-protocols-mapviewbase">MapViewBase</a></code>, this function removes first <code>LocationIndicator</code>
from previous map view before adding to new one.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">enable</span><span class="p">(</span><span class="k">for</span> <span class="nv">mapView</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-mapviewbase">MapViewBase</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapView</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-explore-api-reference-..-protocols-mapviewbase">MapViewBase</a></code> instance.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC7disableyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/disable()"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC7disableyyF">disable()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This function removes <code>LocationIndicator</code> from map view.
If <code>LocationIndicator</code> was not added to any map view yet, this function does nothing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">disable</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC06updateB0yyAA0B0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/updateLocation(_:)"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC06updateB0yyAA0B0VF">updateLocation(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Updates the indicator to a new location.
If accuracy visualized is set to <code>true</code> the field <code><a href="../Structs/Location.html#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">Location.horizontalAccuracyInMeters</a></code>
determines the size of the accuracy indicator halo.</p>
<p>The altitude of the location is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">updateLocation</span><span class="p">(</span><span class="n">_</span> <span class="nv">location</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-location">Location</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>location</em>
</code>
</td>
<td>
<div>
<p>The updated location of the user.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC06updateB0_12cameraUpdateyAA0B0V_AA09MapCameraF0CtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/updateLocation(_:cameraUpdate:)"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC06updateB0_12cameraUpdateyAA0B0V_AA09MapCameraF0CtF">updateLocation(_:<wbr/>cameraUpdate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Updates the indicator to a new location and applies a camera update at the same time.</p>
<p>Does nothing if the indicator instance is not enabled.
If accuracy visualized is set to <code>true</code> the field <code><a href="../Structs/Location.html#/s:7heresdk8LocationV26horizontalAccuracyInMetersSdSgvp">Location.horizontalAccuracyInMeters</a></code>
determines the size of the accuracy indicator halo.</p>
<p>The altitude of the location is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">updateLocation</span><span class="p">(</span><span class="n">_</span> <span class="nv">location</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-location">Location</a></span><span class="p">,</span> <span class="nv">cameraUpdate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraupdate">MapCameraUpdate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>location</em>
</code>
</td>
<td>
<div>
<p>The updated location of the user.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>cameraUpdate</em>
</code>
</td>
<td>
<div>
<p>The update to apply to the camera.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC16setMarker3dModel_5scale4typeyAA16MapMarker3DModelC_SdAC10MarkerTypeOtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setMarker3dModel(_:scale:type:)"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC16setMarker3dModel_5scale4typeyAA16MapMarker3DModelC_SdAC10MarkerTypeOtF">setMarker3dModel(_:<wbr/>scale:<wbr/>type:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type.
The 3D model should be oriented with y axis up and thus standing on the x/z plane where the
z axis is the depth. The direction in which the location indicator is pointing is the
positive z axis. Please note that only MapMarker3DModel created from *.obj files are
supported. Models created from Mesh will be ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.27.0. Please use the overloaded method with `RenderSize.Unit` instead.")</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">setMarker3dModel</span><span class="p">(</span><span class="n">_</span> <span class="nv">model</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker3dmodel">MapMarker3DModel</a></span><span class="p">,</span> <span class="nv">scale</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt">LocationIndicator</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-locationindicator-markertype">MarkerType</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>model</em>
</code>
</td>
<td>
<div>
<p>The MapMarker3DModel object to be displayed for the specified type. Only models
created from obj files are supported. Those created from mesh will be ignored.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>scale</em>
</code>
</td>
<td>
<div>
<p>The scaling which will be applied to the marker model. As the size of the
location marker should be aligned on devices with different resolutions the
scale factor is applied relative to the ppi value and thus differs from the
scale which is passed to <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker3d">MapMarker3D</a></code> objects.
Meter is used for the unit of the map marker 3d model coordinate system.
For historical reason, the scale factor is internally devided by 6.
To display a unit qube of 1x1x1 meter as is, please use a scale value of 6.0.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>type</em>
</code>
</td>
<td>
<div>
<p>The type of location marker for which the marker 3d model should be replaced.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC16setMarker3dModel_5scale4type14renderSizeUnityAA16MapMarker3DModelC_SdAC10MarkerTypeOAA06RenderJ0V0K0OtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setMarker3dModel(_:scale:type:renderSizeUnit:)"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC16setMarker3dModel_5scale4type14renderSizeUnityAA16MapMarker3DModelC_SdAC10MarkerTypeOAA06RenderJ0V0K0OtF">setMarker3dModel(_:<wbr/>scale:<wbr/>type:<wbr/>renderSizeUnit:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker3dmodel">MapMarker3DModel</a></code> asset to be displayed as location indicator for a specified type.
The 3D model should be oriented with y axis up and thus standing on the x/z plane where the
z axis is the depth. The direction in which the location indicator is pointing is the
positive z axis. Please note that only <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker3dmodel">MapMarker3DModel</a></code> created from <code>obj</code> files are
supported. Models created from Mesh will be ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setMarker3dModel</span><span class="p">(</span><span class="n">_</span> <span class="nv">model</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker3dmodel">MapMarker3DModel</a></span><span class="p">,</span> <span class="nv">scale</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt">LocationIndicator</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-locationindicator-markertype">MarkerType</a></span><span class="p">,</span> <span class="nv">renderSizeUnit</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-rendersize">RenderSize</a></span><span class="o">.</span><span class="kt">Unit</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>model</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapmarker3dmodel">MapMarker3DModel</a></code> object to be displayed for the specified type. Only models
created from <code>obj</code> files are supported. Those created from mesh will be ignored.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>scale</em>
</code>
</td>
<td>
<div>
<p>A scale factor applied to the marker model.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>type</em>
</code>
</td>
<td>
<div>
<p>The type of location marker for which the marker 3d model should be replaced.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>renderSizeUnit</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-explore-api-reference-..-structs-rendersize-unit">RenderSize.Unit</a></code> specifying how the vertex coordinates of the
3D model are being interpreted. It specifies whether the 3D model is placed in world or
screen coordinate space.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC12setHaloColor_5coloryAC0C5StyleO_So7UIColorCtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setHaloColor(_:color:)"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC12setHaloColor_5coloryAC0C5StyleO_So7UIColorCtF">setHaloColor(_:<wbr/>color:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the color of the accuracy indicator halo for a given style.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setHaloColor</span><span class="p">(</span><span class="n">_</span> <span class="nv">style</span><span class="p">:</span> <span class="kt">LocationIndicator</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-locationindicator-indicatorstyle">IndicatorStyle</a></span><span class="p">,</span> <span class="nv">color</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>style</em>
</code>
</td>
<td>
<div>
<p>The type of IndicatorStyle for which the color should be assigned.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>color</em>
</code>
</td>
<td>
<div>
<p>The color to be applied to the halo for a specified IndicatorStyle.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17LocationIndicatorC12getHaloColorySo7UIColorCAC0C5StyleOF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getHaloColor(_:)"></a>
<a class="token" href="#/s:7heresdk17LocationIndicatorC12getHaloColorySo7UIColorCAC0C5StyleOF">getHaloColor(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Retrieves the color of the accuracy indicator halo for the requested IndicatorStyle.
The default color is a translucent turquoise (rgba(0, 199, 194, 76)) for all IndicatorStyle settings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getHaloColor</span><span class="p">(</span><span class="n">_</span> <span class="nv">style</span><span class="p">:</span> <span class="kt">LocationIndicator</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-locationindicator-indicatorstyle">IndicatorStyle</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">UIColor</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>style</em>
</code>
</td>
<td>
<div>
<p>The type of IndicatorStyle for which the color should be returned.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The color of the halo for the specified IndicatorStyle.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
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
