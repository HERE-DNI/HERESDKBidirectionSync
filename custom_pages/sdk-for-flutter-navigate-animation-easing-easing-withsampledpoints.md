---
title: "Easing.withSampledPoints constructor"
slug: "sdk-for-flutter-navigate-animation-easing-easing-withsampledpoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Easing.withSampledPoints.html -->


<div>
<h1>Easing.withSampledPoints constructor</h1></div>

Easing.withSampledPoints(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a>&gt; points</li>
</ol>)
    

<p>Creates an instance of customized <a href="/sdk-for-flutter-navigate-animation-easing-class">Easing</a> using a specified number of points describing an
easing function.</p>
<ul>
<li><code>points</code> List of sampled data points that define an easing function.
X describes normalized time values in the range [0, 1].
Y describes normalized animated value changes. Values can fall outside of the range [0, 1]. During
an animation run animated target value is multiplied with Y value. In case resulting animated target value
falls outside of its own supported range it will be clamped to its range (e.g. when negative values used for
color animation).
X values must increase monotonically.
There must be at least 2 data points specified. The first point's X value must be 0, the last point's
X value must be 1.
During an animation run for any given time value X' from the animation engine that
satisfies the relation X(i) &lt; X' &lt; X(i+1) for the given X data points the corresponding
Y' value will be calculated by linearly interpolating between Y(i) and Y(i+1) data points.
The higher the sampling rate of the easing curve used for the data points the more precise the results.
In order to achieve the same animation precision for animations with different durations
(shorter vs longer) it is recommended to use a higher sampling rate for longer animation duration.</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-animation-easinginstantiationexception-class">EasingInstantiationException</a>. Instantiation error in case of invalid input parameters.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory Easing.withSampledPoints(List&lt;Point2D&gt; points) =&gt; $prototype.withSampledPoints(points);</code></pre>

 



</div>
`
}</HTMLBlock>
