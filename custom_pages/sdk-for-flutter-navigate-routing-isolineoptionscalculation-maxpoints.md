---
title: "maxPoints property"
slug: "sdk-for-flutter-navigate-routing-isolineoptionscalculation-maxpoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- maxPoints.html -->


<div>
<h1>maxPoints property</h1></div>

        
        int?
        maxPoints
<div class="features">getter/setter pair</div>


<p>Limits the number of points in the resulting isoline polygon. If the
isoline consists of multiple polygons, the sum of points from all
polygons is considered. Note that this parameter does not affect the calculation,
but the shape of the polygon. Look at <a href="sdk-for-flutter-navigate-routing-isolinecalculationmode">IsolineCalculationMode</a> parameter
to optimize performance.
A higher value will result in a more accurate polygon shape. Rendering a polygon
with a high number of points can negatively impact rendering performance.
The minimum allowed value is 30, lower values will be ignored.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? maxPoints;</code></pre>

 



</div>
`
}</HTMLBlock>
