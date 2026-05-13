---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-venueservice"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- VenueService.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueService"></a>
<a title="VenueService Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-venues">Venues</a>
<img alt="" id="carat" src="../img/carat.png"/>
        VenueService Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VenueService</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueService</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueService</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueService</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Offers methods to download venues. Use of this
object does not necessitate Map involvement.</p>
<p>
Before loading the venues, initialize the venue service
with one of the start methods.
</p>
<p>
The venue service is online only. Even if there is a cached
venue on the device, the venue service requires an online
connection to check if the venue is available for the user.
</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC10Int32Arraya"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/Int32Array"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC10Int32Arraya">Int32Array</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">Int32Array</span> <span class="o">=</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC11StringArraya"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/StringArray"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC11StringArraya">StringArray</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">StringArray</span> <span class="o">=</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC0B8InfoLista"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/VenueInfoList"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC0B8InfoLista">VenueInfoList</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">VenueInfoList</span> <span class="o">=</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venueinfo">VenueInfo</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC0B19OptionalFeatureLista"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/VenueOptionalFeatureList"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC0B19OptionalFeatureLista">VenueOptionalFeatureList</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">VenueOptionalFeatureList</span> <span class="o">=</span> <span class="p">[</span><span class="kt">VenueService</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venueservice-venueoptionalfeature">VenueOptionalFeature</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC9languagesSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/languages"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC9languagesSaySSGvp">languages</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The languages available in the venue service.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">languages</span><span class="p">:</span> <span class="kt">VenueService</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueService.html#/s:7heresdk12VenueServiceC11StringArraya">StringArray</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC8languageSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/language"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC8languageSSvp">language</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The active language.
The venue service will try to load
a venue with a translation in the active language. If such translation doesn’t
exist, a venue will be loaded in its default language.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">language</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC0B15OptionalFeatureO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VenueOptionalFeature"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC0B15OptionalFeatureO">VenueOptionalFeature</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional features enum</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-venueservice-venueoptionalfeature">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VenueOptionalFeature</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC4stopyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/stop()"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC4stopyyF">stop()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Stops the venue service.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">stop</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC03addC8DelegateyyAA0bcE0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addServiceDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC03addC8DelegateyyAA0bcE0_pF">addServiceDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a service delegate. The delegate
is not added if it is <code>nil</code> or is already present in the list of
delegates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addServiceDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-venueservicedelegate">VenueServiceDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The service delegate to add.</p>
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
<a name="/s:7heresdk12VenueServiceC06removeC8DelegateyyAA0bcE0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeServiceDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC06removeC8DelegateyyAA0bcE0_pF">removeServiceDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a service delegate. The delegate
is not removed if it is not present in the list of delegates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeServiceDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-venueservicedelegate">VenueServiceDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The service delegate to remove.</p>
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
<a name="/s:7heresdk12VenueServiceC03addB8DelegateyyAA0bE0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC03addB8DelegateyyAA0bE0_pF">addVenueDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a venue delegate. The delegate
is not added if it is <code>nil</code> or is already present in the list of
delegates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-venuedelegate">VenueDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The venue delegate to add.</p>
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
<a name="/s:7heresdk12VenueServiceC06removeB8DelegateyyAA0bE0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeVenueDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC06removeB8DelegateyyAA0bE0_pF">removeVenueDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a venue delegate. The delegate
is not removed if it is not present in the list of delegates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeVenueDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-venuedelegate">VenueDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The venue delegate to remove.</p>
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
<a name="/s:7heresdk12VenueServiceC03addB11MapDelegateyyAA0beF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueMapDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC03addB11MapDelegateyyAA0beF0_pF">addVenueMapDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a venue map delegate. The delegate
is not added if it is <code>nil</code> or is already present in the list of
delegates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueMapDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-venuemapdelegate">VenueMapDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The venue map delegate to add.</p>
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
<a name="/s:7heresdk12VenueServiceC06removeB11MapDelegateyyAA0beF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeVenueMapDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC06removeB11MapDelegateyyAA0beF0_pF">removeVenueMapDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a venue map delegate. The delegate
is not removed if it is not present in the list of delegates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeVenueMapDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-venuemapdelegate">VenueMapDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The venue map delegate to remove.</p>
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
<a name="/s:7heresdk12VenueServiceC13getInitStatusAA0bceF0OyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getInitStatus()"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC13getInitStatusAA0bceF0OyF">getInitStatus()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets an initialization status.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getInitStatus</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-venueserviceinitstatus">VenueServiceInitStatus</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The initialization status.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC13isInitializedSbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/isInitialized()"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC13isInitializedSbyF">isInitialized()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Checks if the venue service is initialized.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">isInitialized</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code> if the venue service is initialized and <code>false</code> otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC03addB6ToLoad7venueIdys5Int32V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueToLoad(venueId:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC03addB6ToLoad7venueIdys5Int32V_tF">addVenueToLoad(venueId:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a venue to the loading queue.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueToLoad</span><span class="p">(</span><span class="nv">venueId</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>venueId</em>
</code>
</td>
<td>
<div>
<p>The id of the venue to load.</p>
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
<a name="/s:7heresdk12VenueServiceC03addB6ToLoad15venueIdentifierySS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueToLoad(venueIdentifier:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC03addB6ToLoad15venueIdentifierySS_tF">addVenueToLoad(venueIdentifier:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a venue to the loading queue.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueToLoad</span><span class="p">(</span><span class="nv">venueIdentifier</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>venueIdentifier</em>
</code>
</td>
<td>
<div>
<p>The id of the venue to load.</p>
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
<a name="/s:7heresdk12VenueServiceC6setHrn3hrnySS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setHrn(hrn:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC6setHrn3hrnySS_tF">setHrn(hrn:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets HRN of platform catalog.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setHrn</span><span class="p">(</span><span class="nv">hrn</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>hrn</em>
</code>
</td>
<td>
<div>
<p>The HRN of platform catalog.</p>
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
<a name="/s:7heresdk12VenueServiceC22setLabeltextPreference13labelTextPrefySaySSG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setLabeltextPreference(labelTextPref:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC22setLabeltextPreference13labelTextPrefySaySSG_tF">setLabeltextPreference(labelTextPref:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets override labelTextPreference for labels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setLabeltextPreference</span><span class="p">(</span><span class="nv">labelTextPref</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>labelTextPref</em>
</code>
</td>
<td>
<div>
<p>The list of string override labelTextPreference.</p>
<p>
“OCCUPANT_NAMES” - To display only occupant names on map as a label text. Example: Boutique Du Chocolat for id 7348
</p>
<p>
“SPACE_NAME” - To display only space names on map as a label text. Example: Family Services/First Aid for id 7348
</p>
<p>
“SPACE_TYPE_NAME” - To display only space types on map as a label text. Example: DEFIBRILLATOR for id 7348
</p>
<p>
“SPACE_CATEGORY_NAME” - To display only space categories on map as a label text. Example: SAFETY for id 7348
</p>
<p>
“INTERNAL_ADDRESS” - To display only internal addresses on map as a label text. Example: 51/D for id 7348
</p>
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
<a name="/s:7heresdk12VenueServiceC14loadTopologiesyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadTopologies()"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC14loadTopologiesyyF">loadTopologies()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Lets user load topologies for current session</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">loadTopologies</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC20loadOptionalFeatures19optionalFeatureListySayAC0beH0OG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/loadOptionalFeatures(optionalFeatureList:)"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC20loadOptionalFeatures19optionalFeatureListySayAC0beH0OG_tF">loadOptionalFeatures(optionalFeatureList:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Lets user load optional features for current session.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">loadOptionalFeatures</span><span class="p">(</span><span class="nv">optionalFeatureList</span><span class="p">:</span> <span class="kt">VenueService</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueService.html#/s:7heresdk12VenueServiceC0B19OptionalFeatureLista">VenueOptionalFeatureList</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>optionalFeatureList</em>
</code>
</td>
<td>
<div>
<p>The list of optional feature enum VenueOptionalFeature.</p>
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

</div>
`
}</HTMLBlock>
