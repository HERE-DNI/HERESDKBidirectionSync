---
title: "startAngularPanning abstract method"
slug: "sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-startangularpanning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAngularPanning.html -->


<div>
<h1>startAngularPanning abstract method</h1></div>

void
startAngularPanning(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-custompanningdata-class">CustomPanningData</a>? nextCustomPanningData, </li>
<li><a href="/sdk-for-flutter-navigate-navigation-spatialaudiocuepanningspatialazimuthstarted">SpatialAudioCuePanningspatialAzimuthStarted</a> azimuthCallback</li>
</ol>)

      

    

<p>This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer.</p>
<p>An optional custom value for <a href="/sdk-for-flutter-navigate-navigation-custompanningdata-estimatedaudiocueduration">CustomPanningData.estimatedAudioCueDuration</a>,
<a href="/sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees">CustomPanningData.initialAzimuthInDegrees</a>,  or its <a href="/sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees">CustomPanningData.sweepAzimuthInDegrees</a>
can be here defined if the default data does not fully match the utilized Language or TTS engine
or angle expectations.
If startAngularPanning is called to spatialize the audio cue of a new maneuver before the full
completion of a previous spatial audio trajectory, then <a href="/sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a> will retrieve
the azimuth values of the new maneuver.</p>
<ul>
<li>
<p><code>nextCustomPanningData</code> Defines a new set of values related to spatial audio panning.
When <a href="/sdk-for-flutter-navigate-navigation-custompanningdata-class">CustomPanningData</a> is initialized as <code>null</code>, the default set of values provided by HERE SDK
will be used instead.</p>
</li>
<li>
<p><code>azimuthCallback</code> Callback that will signal the next azimuth required to complete a spatial audio trajectory
once the angular panning has started.
Azimuth angular values are retrieved individually until the full duration of the audio trajectory
has been reached,
or a new text message has started its angular panning.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startAngularPanning(CustomPanningData? nextCustomPanningData, SpatialAudioCuePanningspatialAzimuthStarted azimuthCallback);</code></pre>

 



</div>
`
}</HTMLBlock>
