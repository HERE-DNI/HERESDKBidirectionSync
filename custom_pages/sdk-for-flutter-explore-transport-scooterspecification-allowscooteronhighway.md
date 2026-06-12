---
title: "allowScooterOnHighway property"
slug: "sdk-for-flutter-explore-transport-scooterspecification-allowscooteronhighway"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- allowScooterOnHighway.html -->


<div>
<h1>allowScooterOnHighway property</h1></div>

        
        bool
        allowScooterOnHighway
<div class="features">getter/setter pair</div>


<p>Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
allowed to use highways and <code>false</code> means otherwise.
Defaults to <code>false</code>.
Note that there is a similar parameter in <code>AvoidanceOptions</code>, to disallow highway usage,
see <code>RoadFeatures.CONTROLLED_ACCESS_HIGHWAY</code>.
As the avoidance options takes precedence, if this parameter is also used, then
scooters are not allowed to use highways even if <code>allowHighway</code> is set to <code>true</code>.
However, if no alternative route is possible, the calculated route may use highways.
In such a case, a <code>SectionNotice</code> will be provided in the related <code>Section</code> to indicate that
the highway usage restriction is violated on this route.
A few examples:</p>
<p>1 - If no avoidance option is set, and <code>allowHighway = false</code>, when no route is found without
highway usage, a notice is received.</p>
<p>2 - If no avoidance option is set, and <code>allowHighway = true</code>, when no route is found without
highway usage, no notice is received.</p>
<p>3 - If only <code>avoid[features] = controlledAccessHighway</code> is set, when no route is found without
highway usage, a notice is received.</p>
<p>4 - If both <code>avoid[features] = controlledAccessHighway</code> and <code>allowHighway = true</code> are set,
when no route is found without highway usage, a notice is received.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool allowScooterOnHighway;</code></pre>

 



</div>
`
}</HTMLBlock>
