---
title: "VenueMap"
slug: "sdk-for-ios-navigate-api-reference-classes-venuemap"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueMap"></a>
<a title="VenueMap Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-venues">Venues</a>

        VenueMap Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VenueMap</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueMap</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueMap</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueMap</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Connects a map with venues. When the <code>VenueMap</code> is started,
venues can be seen on the map as interactive models. The user can switch drawings and levels,
change a visual style of geometries and related labels inside the venue etc.
After constructing the <code>VenueMap</code>, delegates
for relevant events should be added to the object. <code>VenueMap</code> is an add-on to
the base map functionality with its own content loading and cache. For this reason, in certain
situations there may be a small delay before the venue is visible.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC0B8InfoLista"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/VenueInfoList"></a>
<a class="token" href="#/s:7heresdk8VenueMapC0B8InfoLista">VenueInfoList</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">VenueInfoList</span> <span class="o">=</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venueinfo">VenueInfo</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC12venueServiceAA0bE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/venueService"></a>
<a class="token" href="#/s:7heresdk8VenueMapC12venueServiceAA0bE0Cvp">venueService</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-venueservice">VenueService</a></code> object.
It can be used to search and get the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code> objects.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">venueService</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venueservice">VenueService</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC08selectedB0AA0B0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/selectedVenue"></a>
<a class="token" href="#/s:7heresdk8VenueMapC08selectedB0AA0B0CSgvp">selectedVenue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The selected venue or <code>nil</code> if no venue is selected.
Use <code>nil</code> to deselect the venue.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">selectedVenue</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC03addB5Async7venueIdys5Int32V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueAsync(venueId:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03addB5Async7venueIdys5Int32V_tF">addVenueAsync(venueId:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloads and adds a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code> to the <code>VenueMap</code>.
Method will do nothing if the venue already exists on the venue map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueAsync</span><span class="p">(</span><span class="nv">venueId</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
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
<p>The ID of the venue to download and add.</p>
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
<a name="/s:7heresdk8VenueMapC03addB5Async15venueIdentifierySS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueAsync(venueIdentifier:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03addB5Async15venueIdentifierySS_tF">addVenueAsync(venueIdentifier:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloads and adds a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code> to the <code>VenueMap</code>.
Method will do nothing if the venue already exists on the venue map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueAsync</span><span class="p">(</span><span class="nv">venueIdentifier</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
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
<p>The ID of the venue to download and add.</p>
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
<a name="/s:7heresdk8VenueMapC03addB5Async7venueId10completionys5Int32V_yAA0B9ErrorCodeOSgctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueAsync(venueId:completion:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03addB5Async7venueId10completionys5Int32V_yAA0B9ErrorCodeOSgctF">addVenueAsync(venueId:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloads and adds a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code> to the <code>VenueMap</code>.
Method will do nothing if the venue already exists on the venue map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueAsync</span><span class="p">(</span><span class="nv">venueId</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Venues.html#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a></span><span class="p">)</span></code></pre>
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
<p>The ID of the venue to download and add.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback to receives the error while venue load on the main thread.</p>
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
<a name="/s:7heresdk8VenueMapC03addB5Async15venueIdentifier10completionySS_yAA0B9ErrorCodeOSgctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueAsync(venueIdentifier:completion:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03addB5Async15venueIdentifier10completionySS_yAA0B9ErrorCodeOSgctF">addVenueAsync(venueIdentifier:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloads and adds a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code> to the <code>VenueMap</code>.
Method will do nothing if the venue already exists on the venue map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueAsync</span><span class="p">(</span><span class="nv">venueIdentifier</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Venues.html#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a></span><span class="p">)</span></code></pre>
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
<p>The ID of the venue to download and add.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback to receives the error while venue load on the main thread.</p>
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
<a name="/s:7heresdk8VenueMapC06removeB05venueyAA0B0C_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeVenue(venue:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06removeB05venueyAA0B0C_tF">removeVenue(venue:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code> from the <code>VenueMap</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeVenue</span><span class="p">(</span><span class="nv">venue</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>venue</em>
</code>
</td>
<td>
<div>
<p>The venue to remove.</p>
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
<a name="/s:7heresdk8VenueMapC06selectB5Async7venueIdys5Int32V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/selectVenueAsync(venueId:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06selectB5Async7venueIdys5Int32V_tF">selectVenueAsync(venueId:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloads a <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code> if needed and selects a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">selectVenueAsync</span><span class="p">(</span><span class="nv">venueId</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
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
<p>The ID of the venue to download and select.</p>
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
<a name="/s:7heresdk8VenueMapC06selectB5Async15venueIdentifierySS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/selectVenueAsync(venueIdentifier:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06selectB5Async15venueIdentifierySS_tF">selectVenueAsync(venueIdentifier:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloads a <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code> if needed and selects a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">selectVenueAsync</span><span class="p">(</span><span class="nv">venueIdentifier</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
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
<p>The ID of the venue to download and select.</p>
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
<a name="/s:7heresdk8VenueMapC06selectB5Async7venueId10completionys5Int32V_yAA0B9ErrorCodeOSgctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/selectVenueAsync(venueId:completion:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06selectB5Async7venueId10completionys5Int32V_yAA0B9ErrorCodeOSgctF">selectVenueAsync(venueId:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloads a <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code> if needed and selects a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">selectVenueAsync</span><span class="p">(</span><span class="nv">venueId</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Venues.html#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a></span><span class="p">)</span></code></pre>
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
<p>The ID of the venue to download and select.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback to receives the error while venue load on the main thread.</p>
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
<a name="/s:7heresdk8VenueMapC06selectB5Async15venueIdentifier10completionySS_yAA0B9ErrorCodeOSgctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/selectVenueAsync(venueIdentifier:completion:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06selectB5Async15venueIdentifier10completionySS_yAA0B9ErrorCodeOSgctF">selectVenueAsync(venueIdentifier:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Downloads a <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code> if needed and selects a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">selectVenueAsync</span><span class="p">(</span><span class="nv">venueIdentifier</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Venues.html#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a></span><span class="p">)</span></code></pre>
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
<p>The ID of the venue to download and select.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback to receives the error while venue load on the main thread.</p>
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
<a name="/s:7heresdk8VenueMapC06cancelB9SelectionSbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/cancelVenueSelection()"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06cancelB9SelectionSbyF">cancelVenueSelection()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Attempts to cancel venue loading and selection
that may currently be in progress.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">cancelVenueSelection</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code> if a venue was about to load and <code>false</code> otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC03getB08positionAA0B0CSgAA14GeoCoordinatesV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getVenue(position:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03getB08positionAA0B0CSgAA14GeoCoordinatesV_tF">getVenue(position:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tries to find a <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code> at the specified geographic coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getVenue</span><span class="p">(</span><span class="nv">position</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>position</em>
</code>
</td>
<td>
<div>
<p>Geographic coordinates where a venue is located.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Venue or <code>nil</code> if there is no venue at the specified geographic coordinates.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC11getGeometry8positionAA0bE0CSgAA14GeoCoordinatesV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getGeometry(position:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC11getGeometry8positionAA0bE0CSgAA14GeoCoordinatesV_tF">getGeometry(position:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tries to find a <code><a href="sdk-for-ios-navigate-api-reference-classes-venuegeometry">VenueGeometry</a></code> at the specified geographic coordinates
in the selected <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code> in the currently selected <code><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getGeometry</span><span class="p">(</span><span class="nv">position</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuegeometry">VenueGeometry</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>position</em>
</code>
</td>
<td>
<div>
<p>Geographic coordinates where the geometry is located.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Geometry or <code>nil</code> if there is no geometry at the specified geographic coordinates.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC03addB17LifecycleDelegateyyAA0beF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueLifecycleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03addB17LifecycleDelegateyyAA0beF0_pF">addVenueLifecycleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a venue lifecycle delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueLifecycleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venuelifecycledelegate">VenueLifecycleDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to add.</p>
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
<a name="/s:7heresdk8VenueMapC06removeB17LifecycleDelegateyyAA0beF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeVenueLifecycleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06removeB17LifecycleDelegateyyAA0beF0_pF">removeVenueLifecycleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a venue lifecycle delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeVenueLifecycleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venuelifecycledelegate">VenueLifecycleDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to remove.</p>
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
<a name="/s:7heresdk8VenueMapC03addbC17LifecycleDelegateyyAA0bceF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueMapLifecycleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03addbC17LifecycleDelegateyyAA0bceF0_pF">addVenueMapLifecycleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a venue map lifecycle delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueMapLifecycleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venuemaplifecycledelegate">VenueMapLifecycleDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to add.</p>
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
<a name="/s:7heresdk8VenueMapC06removebC17LifecycleDelegateyyAA0bceF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeVenueMapLifecycleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06removebC17LifecycleDelegateyyAA0bceF0_pF">removeVenueMapLifecycleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a venue map lifecycle delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeVenueMapLifecycleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venuemaplifecycledelegate">VenueMapLifecycleDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to remove.</p>
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
<a name="/s:7heresdk8VenueMapC03addB17SelectionDelegateyyAA0beF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueSelectionDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03addB17SelectionDelegateyyAA0beF0_pF">addVenueSelectionDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a venue selection delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueSelectionDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venueselectiondelegate">VenueSelectionDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to add.</p>
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
<a name="/s:7heresdk8VenueMapC06removeB17SelectionDelegateyyAA0beF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeVenueSelectionDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06removeB17SelectionDelegateyyAA0beF0_pF">removeVenueSelectionDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a venue selection delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeVenueSelectionDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venueselectiondelegate">VenueSelectionDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to remove.</p>
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
<a name="/s:7heresdk8VenueMapC27addDrawingSelectionDelegateyyAA0befG0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addDrawingSelectionDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC27addDrawingSelectionDelegateyyAA0befG0_pF">addDrawingSelectionDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a drawing selection delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addDrawingSelectionDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venuedrawingselectiondelegate">VenueDrawingSelectionDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to add.</p>
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
<a name="/s:7heresdk8VenueMapC30removeDrawingSelectionDelegateyyAA0befG0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeDrawingSelectionDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC30removeDrawingSelectionDelegateyyAA0befG0_pF">removeDrawingSelectionDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a drawing selection delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeDrawingSelectionDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venuedrawingselectiondelegate">VenueDrawingSelectionDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to remove.</p>
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
<a name="/s:7heresdk8VenueMapC25addLevelSelectionDelegateyyAA0befG0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addLevelSelectionDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC25addLevelSelectionDelegateyyAA0befG0_pF">addLevelSelectionDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a level selection delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addLevelSelectionDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venuelevelselectiondelegate">VenueLevelSelectionDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to add.</p>
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
<a name="/s:7heresdk8VenueMapC28removeLevelSelectionDelegateyyAA0befG0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeLevelSelectionDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC28removeLevelSelectionDelegateyyAA0befG0_pF">removeLevelSelectionDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a level selection delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeLevelSelectionDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venuelevelselectiondelegate">VenueLevelSelectionDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The delegate to remove.</p>
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
<a name="/s:7heresdk8VenueMapC03addB16InfoListDelegateyyAA0bef8ListenerG0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addVenueInfoListDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03addB16InfoListDelegateyyAA0bef8ListenerG0_pF">addVenueInfoListDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a listener to handle the completion of the asynchronous venue info list retrieval.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addVenueInfoListDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venueinfolistlistenerdelegate">VenueInfoListListenerDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The listener to add.</p>
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
<a name="/s:7heresdk8VenueMapC06removeB16InfoListDelegateyyAA0bef8ListenerG0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeVenueInfoListDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC06removeB16InfoListDelegateyyAA0bef8ListenerG0_pF">removeVenueInfoListDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a listener for the asynchronous venue info list retrieval.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeVenueInfoListDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-venueinfolistlistenerdelegate">VenueInfoListListenerDelegate</a></span><span class="p">)</span></code></pre>
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
<p>The listener to remove.</p>
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
<a name="/s:7heresdk8VenueMapC03getB8InfoListSayAA0bE0CGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getVenueInfoList()"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03getB8InfoListSayAA0bE0CGyF">getVenueInfoList()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-api-reference-classes-venueinfo">VenueInfo</a></code> contains venue id and name.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getVenueInfoList</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">VenueMap</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueMap.html#/s:7heresdk8VenueMapC0B8InfoLista">VenueInfoList</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>returns the list of object of <code><a href="sdk-for-ios-navigate-api-reference-classes-venueinfo">VenueInfo</a></code>.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC03getB8InfoList10completionSayAA0bE0CGyAA0B9ErrorCodeOSgc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getVenueInfoList(completion:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03getB8InfoList10completionSayAA0bE0CGyAA0B9ErrorCodeOSgc_tF">getVenueInfoList(completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-api-reference-classes-venueinfo">VenueInfo</a></code> contains venue id and name.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getVenueInfoList</span><span class="p">(</span><span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Venues.html#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">VenueMap</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueMap.html#/s:7heresdk8VenueMapC0B8InfoLista">VenueInfoList</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback to receives the error while venue load on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>returns the list of object of <code><a href="sdk-for-ios-navigate-api-reference-classes-venueinfo">VenueInfo</a></code>.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC03getB13InfoListAsyncyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getVenueInfoListAsync()"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03getB13InfoListAsyncyyF">getVenueInfoListAsync()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-api-reference-classes-venueinfo">VenueInfo</a></code> contains venue id and name.
Downloads the list of <code><a href="sdk-for-ios-navigate-api-reference-classes-venueinfo">VenueInfo</a></code> asynchronously.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getVenueInfoListAsync</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC03getB13InfoListAsync10completionyyAA0B9ErrorCodeOSgc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getVenueInfoListAsync(completion:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC03getB13InfoListAsync10completionyyAA0B9ErrorCodeOSgc_tF">getVenueInfoListAsync(completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-api-reference-classes-venueinfo">VenueInfo</a></code> contains venue id and name.
Downloads the list of <code><a href="sdk-for-ios-navigate-api-reference-classes-venueinfo">VenueInfo</a></code> asynchronously.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getVenueInfoListAsync</span><span class="p">(</span><span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Venues.html#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback to receive the list of venue info if successful.</p>
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
<a name="/s:7heresdk8VenueMapC11getTopology8positionAA0bE0CSgAA14GeoCoordinatesV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getTopology(position:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC11getTopology8positionAA0bE0CSgAA14GeoCoordinatesV_tF">getTopology(position:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tries to find a <code><a href="sdk-for-ios-navigate-api-reference-classes-venuetopology">VenueTopology</a></code> at the specified geographic coordinates
in the selected <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code> in the currently selected <code><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getTopology</span><span class="p">(</span><span class="nv">position</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuetopology">VenueTopology</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>position</em>
</code>
</td>
<td>
<div>
<p>Geographic coordinates where the topology is located.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Topology or <code>nil</code> if there is no topology at the specified geographic coordinates.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8VenueMapC12getCrosswalk8positionAA0E0CSgAA14GeoCoordinatesV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getCrosswalk(position:)"></a>
<a class="token" href="#/s:7heresdk8VenueMapC12getCrosswalk8positionAA0E0CSgAA14GeoCoordinatesV_tF">getCrosswalk(position:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tries to find a <code><a href="sdk-for-ios-navigate-api-reference-classes-crosswalk">Crosswalk</a></code> at the specified geographic coordinates
in the selected <code><a href="sdk-for-ios-navigate-api-reference-classes-venue">Venue</a></code> in the currently selected <code><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getCrosswalk</span><span class="p">(</span><span class="nv">position</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-crosswalk">Crosswalk</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>position</em>
</code>
</td>
<td>
<div>
<p>Geographic coordinates where the crosswalk is located.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Crosswalk or <code>nil</code> if there is no crosswalk at the specified geographic coordinates.</p>
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
} </HTMLBlock>
