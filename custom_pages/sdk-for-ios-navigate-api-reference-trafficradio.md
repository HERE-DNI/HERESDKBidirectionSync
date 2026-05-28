---
title: "TrafficRadio"
slug: "sdk-for-ios-navigate-api-reference-trafficradio"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/TrafficRadio"></a>
<a title="TrafficRadio  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="img/carat.png"/>
        TrafficRadio  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficRadio</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficBroadcastC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficBroadcast"></a>
<a class="token" href="#/s:7heresdk16TrafficBroadcastC">TrafficBroadcast</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A <code>TrafficBroadcast</code> is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a>
format and it can be used when there is no internet connection, so that the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlineroutingengine">OfflineRoutingEngine</a></code>
can utilize traffic data coming over a radio channel. The <code><a href="Classes/TrafficBroadcast.html#/s:7heresdk16TrafficBroadcastC8activateyyF">TrafficBroadcast.activate(...)</a></code> method needs to be called to
receive traffic data events.</p>
<p><strong>Note:</strong> In order to adopt the <code><a href="Traffic.html#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a></code> interface special hardware is required. Talk
to your HERE representative for more details. Only by adopting the <code><a href="Traffic.html#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a></code> interface
you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant
to be used <em>independently</em> from the already included traffic on routes, on the map and from the
HERE backends (when using the <code><a href="sdk-for-ios-navigate-api-reference-classes-trafficengine">TrafficEngine</a></code>).</p>
<p>This class continuously reacts to new locations provided from a location source and acts as a
<code><a href="sdk-for-ios-navigate-api-reference-protocols-locationdelegate">LocationDelegate</a></code>. The location must be updated regardless of calling <code><a href="Classes/TrafficBroadcast.html#/s:7heresdk16TrafficBroadcastC8activateyyF">TrafficBroadcast.activate(...)</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-trafficbroadcast">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficBroadcast</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-locationdelegate">LocationDelegate</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficBroadcast</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficBroadcast</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26TrafficBroadcastParametersV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficBroadcastParameters"></a>
<a class="token" href="#/s:7heresdk26TrafficBroadcastParametersV">TrafficBroadcastParameters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the parameters needed to request the traffic broadcast.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-trafficbroadcastparameters">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficBroadcastParameters</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7TMCDataV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TMCData"></a>
<a class="token" href="#/s:7heresdk7TMCDataV">TMCData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the traffic events in RDS-TMC format.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-tmcdata">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TMCData</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TMCPreferredSidsRequestV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TMCPreferredSidsRequest"></a>
<a class="token" href="#/s:7heresdk23TMCPreferredSidsRequestV">TMCPreferredSidsRequest</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents data used to request the list of preferred SIDs.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-tmcpreferredsidsrequest">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TMCPreferredSidsRequest</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TMCServiceProviderInfoV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TMCServiceProviderInfo"></a>
<a class="token" href="#/s:7heresdk22TMCServiceProviderInfoV">TMCServiceProviderInfo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the service prodiver info in RDS-TMC format.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-tmcserviceproviderinfo">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TMCServiceProviderInfo</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17TMCServiceRequestV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TMCServiceRequest"></a>
<a class="token" href="#/s:7heresdk17TMCServiceRequestV">TMCServiceRequest</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the parameters used to request the traffic broadcast.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-tmcservicerequest">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TMCServiceRequest</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TMCServiceInterfaceP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TMCServiceInterface"></a>
<a class="token" href="#/s:7heresdk19TMCServiceInterfaceP">TMCServiceInterface</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains all outgoing dependencies to the client side.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-tmcserviceinterface">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TMCServiceInterface</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RDSEncryptionKeyV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RDSEncryptionKey"></a>
<a class="token" href="#/s:7heresdk16RDSEncryptionKeyV">RDSEncryptionKey</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the RDS encryption key.
Fields allocation information is described in CEN ISO/CD 14819-6.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-rdsencryptionkey">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RDSEncryptionKey</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24RDSEncryptionKeysRequestV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RDSEncryptionKeysRequest"></a>
<a class="token" href="#/s:7heresdk24RDSEncryptionKeysRequestV">RDSEncryptionKeysRequest</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents data to search for RDS encryption keys.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-rdsencryptionkeysrequest">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RDSEncryptionKeysRequest</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
