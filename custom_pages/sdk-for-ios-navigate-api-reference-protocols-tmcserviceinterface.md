---
title: "sdk-for-ios-navigate-api-reference-protocols-tmcserviceinterface"
slug: "sdk-for-ios-navigate-api-reference-protocols-tmcserviceinterface"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TMCServiceInterface"></a>
<a title="TMCServiceInterface Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-trafficradio">TrafficRadio</a>
<img alt="" id="carat" src="/carat.png"/>
        TMCServiceInterface Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TMCServiceInterface</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TMCServiceInterface</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>Contains all outgoing dependencies to the client side.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TMCServiceInterfaceP07requestB017tmcServiceRequestyAA0bG0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/requestTMCService(tmcServiceRequest:)"></a>
<a class="token" href="#/s:7heresdk19TMCServiceInterfaceP07requestB017tmcServiceRequestyAA0bG0V_tF">requestTMCService(tmcServiceRequest:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called whenever the traffic broadcast needs to be activated.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">requestTMCService</span><span class="p">(</span><span class="nv">tmcServiceRequest</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-tmcservicerequest">TMCServiceRequest</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tmcServiceRequest</em>
</code>
</td>
<td>
<div>
<p>Parameters used to request the traffic broadcast.</p>
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
<a name="/s:7heresdk19TMCServiceInterfaceP19getTMCPreferredSids012tmcPreferredF7RequestSays5UInt8VGAA0efI0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getTMCPreferredSids(tmcPreferredSidsRequest:)"></a>
<a class="token" href="#/s:7heresdk19TMCServiceInterfaceP19getTMCPreferredSids012tmcPreferredF7RequestSays5UInt8VGAA0efI0V_tF">getTMCPreferredSids(tmcPreferredSidsRequest:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called whenever there is a need to get a list of preferred SIDs for a specific area.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getTMCPreferredSids</span><span class="p">(</span><span class="nv">tmcPreferredSidsRequest</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-tmcpreferredsidsrequest">TMCPreferredSidsRequest</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt">UInt8</span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tmcPreferredSidsRequest</em>
</code>
</td>
<td>
<div>
<p>Specifies the area to request the preferred SIDs.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>List of preferred SIDs.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TMCServiceInterfaceP20getRDSEncryptionKeys013rdsEncryptionF7RequestSayAA0E3KeyVGAA0efI0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getRDSEncryptionKeys(rdsEncryptionKeysRequest:)"></a>
<a class="token" href="#/s:7heresdk19TMCServiceInterfaceP20getRDSEncryptionKeys013rdsEncryptionF7RequestSayAA0E3KeyVGAA0efI0V_tF">getRDSEncryptionKeys(rdsEncryptionKeysRequest:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called whenever there is a need to get RDS encryption keys.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getRDSEncryptionKeys</span><span class="p">(</span><span class="nv">rdsEncryptionKeysRequest</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rdsencryptionkeysrequest">RDSEncryptionKeysRequest</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rdsencryptionkey">RDSEncryptionKey</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>rdsEncryptionKeysRequest</em>
</code>
</td>
<td>
<div>
<p>Input data to search for keys.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>RDS encryption keys.</p>
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
