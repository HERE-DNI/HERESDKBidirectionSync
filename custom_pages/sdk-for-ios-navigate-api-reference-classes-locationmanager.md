---
title: "LocationManager"
slug: "sdk-for-ios-navigate-api-reference-classes-locationmanager"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/LocationManager"></a>
<a title="LocationManager Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-other%20classes">Other Classes</a>

        LocationManager Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationManager</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LocationManager</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-locationdelegate">LocationDelegate</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationManager</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LocationManager</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>LocationManager listens to position updates and provides the
map-matched location using the LocationManagerListener.</p>
<p><strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
behaviors. Related APIs may change in future releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationManagerC9sdkEngineAcA09SDKNativeE0C_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:)"></a>
<a class="token" href="#/s:7heresdk15LocationManagerC9sdkEngineAcA09SDKNativeE0C_tKcfc">init(sdkEngine:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of <code>LocationManager</code>.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Instantiation error.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>A SDKEngine instance.</p>
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
<a name="/s:7heresdk15LocationManagerC02onB7UpdatedyyAA0B0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onLocationUpdated(_:)"></a>
<a class="token" href="#/s:7heresdk15LocationManagerC02onB7UpdatedyyAA0B0VF">onLocationUpdated(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called each time a new location is available.
In a navigation context while using the <code><a href="sdk-for-ios-navigate-api-reference-classes-navigator">Navigator</a></code> or <code><a href="sdk-for-ios-navigate-api-reference-classes-visualnavigator">VisualNavigator</a></code>,
it’s required to set the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter for each <code><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></code>
object so that the HERE SDK can map-match the locations properly.
If the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter is missing, the location will be ignored.
For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
parameters for each <code><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></code> object.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onLocationUpdated</span><span class="p">(</span><span class="n">_</span> <span class="nv">location</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></span><span class="p">)</span></code></pre>
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
<p>Current location.</p>
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
<a name="/s:7heresdk15LocationManagerC13setMapMatcher03mapF0yAA0eF0CSg_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setMapMatcher(mapMatcher:)"></a>
<a class="token" href="#/s:7heresdk15LocationManagerC13setMapMatcher03mapF0yAA0eF0CSg_tF">setMapMatcher(mapMatcher:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></code> for exclusive use by <code>LocationManager</code>.</p>
<p><strong>Threading:</strong> This method is asynchronous and performs the switch in an internal thread of <code>LocationManager</code>.
<strong>Note:</strong> After calling this method, the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></code> is owned and used exclusively
by <code>LocationManager</code> in its internal processing thread.
Do not use or access the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></code> elsewhere while it is set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setMapMatcher</span><span class="p">(</span><span class="nv">mapMatcher</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapMatcher</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></code> instance to be used exclusively by <code>LocationManager</code>.</p>
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
<a name="/s:7heresdk15LocationManagerC14takeMapMatcherAA0eF0CSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/takeMapMatcher()"></a>
<a class="token" href="#/s:7heresdk15LocationManagerC14takeMapMatcherAA0eF0CSgyF">takeMapMatcher()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Retrieves and removes the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></code> from <code>LocationManager</code>.
<strong>Note:</strong> After calling this method, <code>LocationManager</code> will no longer use the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></code> at all.
the caller regains full ownership and responsibility for the <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">takeMapMatcher</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmatcher">MapMatcher</a></code> instance previously set, or <code>nil</code> if none was set.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LocationManagerC07MatchedB8Delegate07matchedB8ListeneryAA0dbG0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/MatchedLocationDelegate(matchedLocationListener:)"></a>
<a class="token" href="#/s:7heresdk15LocationManagerC07MatchedB8Delegate07matchedB8ListeneryAA0dbG0_p_tF">MatchedLocationDelegate(matchedLocationListener:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds the <code><a href="sdk-for-ios-navigate-api-reference-protocols-matchedlocationlistener">MatchedLocationListener</a></code> to the subscribtion list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="kt">MatchedLocationDelegate</span><span class="p">(</span><span class="nv">matchedLocationListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-matchedlocationlistener">MatchedLocationListener</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>matchedLocationListener</em>
</code>
</td>
<td>
<div>
<p>Listener to be added to the map matched location updates.</p>
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
<a name="/s:7heresdk15LocationManagerC013removeMatchedB8Listener07matchedbF0yAA0ebF0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMatchedLocationListener(matchedLocationListener:)"></a>
<a class="token" href="#/s:7heresdk15LocationManagerC013removeMatchedB8Listener07matchedbF0yAA0ebF0_p_tF">removeMatchedLocationListener(matchedLocationListener:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes the <code><a href="sdk-for-ios-navigate-api-reference-protocols-matchedlocationlistener">MatchedLocationListener</a></code> from the subscribtion list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMatchedLocationListener</span><span class="p">(</span><span class="nv">matchedLocationListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-matchedlocationlistener">MatchedLocationListener</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>matchedLocationListener</em>
</code>
</td>
<td>
<div>
<p>Listener to be removed from the map matched location updates.</p>
</div>
</td>
</tr>
</tbody>
</table>
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
