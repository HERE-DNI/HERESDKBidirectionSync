---
title: "addCustomWarningProvider abstract method"
slug: "sdk-for-flutter-navigate-warner-warnerengine-addcustomwarningprovider"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addCustomWarningProvider.html -->


<div>
<h1>addCustomWarningProvider abstract method</h1></div>

void
addCustomWarningProvider(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-warner-customwarningprovider-class">CustomWarningProvider</a> customWarningProvider, </li>
<li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a> segmentDataLoaderOptions</li>
</ol>)

      

    

<p>Registers a custom warning provider.</p>
<p>The registered provider participates in warning evaluation and is invoked
to generate custom warnings based on the current vehicle position.</p>
<ul>
<li>
<p><code>customWarningProvider</code> A provider responsible for generating custom warnings.</p>
</li>
<li>
<p><code>segmentDataLoaderOptions</code> Specifies which data should be loaded by the <code>SegmentDataLoader</code>.</p>
</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addCustomWarningProvider(CustomWarningProvider customWarningProvider, SegmentDataLoaderOptions segmentDataLoaderOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
