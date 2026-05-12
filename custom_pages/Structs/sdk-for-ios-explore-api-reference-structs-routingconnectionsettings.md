---
title: "RoutingConnectionSettings Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-routingconnectionsettings"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- RoutingConnectionSettings.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/RoutingConnectionSettings"></a>
<a title="RoutingConnectionSettings Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RoutingConnectionSettings Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct RoutingConnectionSettings : Hashable</code></pre>
</div>
</div>
<p>Defines the settings for the retry logic when connecting to the HERE routing backend.</p>
<p>When a timeout is triggered,
the next connection attempt starts with a increased timeout.
new_timeout = initial_timeout + increment * retry_count</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25RoutingConnectionSettingsV07initialC7TimeoutSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/initialConnectionTimeout"></a>
<a class="token" href="#/s:7heresdk25RoutingConnectionSettingsV07initialC7TimeoutSdvp">initialConnectionTimeout</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the initial time out for connection to the backend.
By default, the initial connection timeout is 5 seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var initialConnectionTimeout: TimeInterval</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25RoutingConnectionSettingsV30connectionTimeoutRetryIncreaseSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectionTimeoutRetryIncrease"></a>
<a class="token" href="#/s:7heresdk25RoutingConnectionSettingsV30connectionTimeoutRetryIncreaseSdvp">connectionTimeoutRetryIncrease</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the increase of the timeout for the transfer of data.
By default, the initial connection increment per timeout 10 seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var connectionTimeoutRetryIncrease: TimeInterval</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25RoutingConnectionSettingsV22initialTransferTimeoutSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/initialTransferTimeout"></a>
<a class="token" href="#/s:7heresdk25RoutingConnectionSettingsV22initialTransferTimeoutSdvp">initialTransferTimeout</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the initial time out for data transfer from the backend.
By default, the initial transfer timeout is 10 seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var initialTransferTimeout: TimeInterval</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25RoutingConnectionSettingsV28transferTimeoutRetryIncreaseSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transferTimeoutRetryIncrease"></a>
<a class="token" href="#/s:7heresdk25RoutingConnectionSettingsV28transferTimeoutRetryIncreaseSdvp">transferTimeoutRetryIncrease</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the increase of the timeout for the connection.
By default, the initial transfer increment per timeout is 2 seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var transferTimeoutRetryIncrease: TimeInterval</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25RoutingConnectionSettingsV13maxRetryCounts5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxRetryCount"></a>
<a class="token" href="#/s:7heresdk25RoutingConnectionSettingsV13maxRetryCounts5Int32Vvp">maxRetryCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the max amount of retries before the route request failes with connection related error codes.
By default, the max amount of retries is 3.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var maxRetryCount: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25RoutingConnectionSettingsV07initialC7Timeout010connectionF13RetryIncrease0e8TransferF008transferfhI003maxH5CountACSd_S3ds5Int32Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(initialConnectionTimeout:connectionTimeoutRetryIncrease:initialTransferTimeout:transferTimeoutRetryIncrease:maxRetryCount:)"></a>
<a class="token" href="#/s:7heresdk25RoutingConnectionSettingsV07initialC7Timeout010connectionF13RetryIncrease0e8TransferF008transferfhI003maxH5CountACSd_S3ds5Int32Vtcfc">init(initialConnectionTimeout:<wbr/>connectionTimeoutRetryIncrease:<wbr/>initialTransferTimeout:<wbr/>transferTimeoutRetryIncrease:<wbr/>maxRetryCount:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(initialConnectionTimeout: TimeInterval = 5, connectionTimeoutRetryIncrease: TimeInterval = 10, initialTransferTimeout: TimeInterval = 10, transferTimeoutRetryIncrease: TimeInterval = 2, maxRetryCount: Int32 = 3)</code></pre>
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



</div>
`
}</HTMLBlock>
