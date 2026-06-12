---
title: "IconProviderCallback typedef"
slug: "sdk-for-flutter-explore-mapview-iconprovidercallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IconProviderCallback.html -->


<div>
<h1>IconProviderCallback typedef</h1></div>

IconProviderCallback =
     void Function(ImageInfo? imageInfo, String? iconDescription, <a href="/sdk-for-flutter-explore-mapview-iconprovidererror">IconProviderError</a>? error)


<p>A callback of this type is invoked when an icon is received from the <a href="/sdk-for-flutter-explore-mapview-iconprovider-class">IconProvider</a> in
the <code>ImageInfo</code> format. The callback provides information about the loaded icon, or an
<a href="/sdk-for-flutter-explore-mapview-iconprovidererror">IconProviderError</a> if one occurred.</p>
<p><code>imageInfo</code> The created <code>ImageInfo</code> containing the icon, or <code>null</code> if an error occurred.</p>
<p><code>iconDescription</code> An English description of the created icon. For example, "Federal Highway"
                  for the road shield icon with the <a href="/sdk-for-flutter-explore-core-routetype">RouteType.level1Road</a> in Brazil.
                  It will be <code>null</code> if an error occurred.</p>
<p><code>error</code> The error that occurred, or <code>null</code> if the icon is loaded successfully.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef IconProviderCallback = void Function(
    ImageInfo? imageInfo, String? iconDescription, IconProviderError? error);</code></pre>

 



</div>
`
}</HTMLBlock>
