---
title: "PlaceCategory Class Reference"
slug: "sdk-for-ios-navigate-classes-placecategory"
---

# PlaceCategory

<div class="declaration">

<div class="language">

``` highlight
public class PlaceCategory
```

``` highlight
extension PlaceCategory: NativeBase
```

``` highlight
extension PlaceCategory: Hashable
```

</div>

</div>

Represents a category of place with different levels of granularity. This class also defines a set of most commonly used categories.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC2idACSS_tcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-id" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC2idACSS_tcfc" class="token"><code>init(id:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(id: String)
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>id</code></em><code> </code></td>
  <td><div>
  <p>Place category ID. The HERE places category system provides three levels of granularity:</p>
  <ol>
  <li>Level 1 represents high level groupings, such as “Eat and drink”. Their IDs take the form “xxx”, for example “100”.</li>
  <li>Level 2 represents logical sub-groups or domains, such as “Eat and Drink / Restaurant”. Their IDs take the form “xxx-xxxx”, for example “100-1000”.</li>
  <li>Level 3 provides the greatest level of granularity about place categorization, such as “Eat and Drink / Restaurant / Casual Dining”. Their IDs take the form “xxx-xxxx-xxxx”, for example “100-1000-0001”. The category ID can be provided as one of the predefined values, such as <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21eatAndDrinkRestaurantSSvpZ"><code>PlaceCategory.eatAndDrinkRestaurant</code></a> or as a literal string that matches one of the category IDs defined by the HERE Search service. Only level 1 and 2 category IDs are predefined. The complete list of supported category IDs, including level 3, can be found online: <a href="https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html">https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html</a>.</li>
  </ol>
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC11eatAndDrinkSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-eatAndDrink" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC11eatAndDrinkSSvpZ" class="token"><code>eatAndDrink</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places where food or beverages are prepared or served.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let eatAndDrink: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21eatAndDrinkRestaurantSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-eatAndDrinkRestaurant" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21eatAndDrinkRestaurantSSvpZ" class="token"><code>eatAndDrinkRestaurant</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment that prepares and serves refreshments and prepared meals.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let eatAndDrinkRestaurant: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC20eatAndDrinkCoffeeTeaSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-eatAndDrinkCoffeeTea" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC20eatAndDrinkCoffeeTeaSSvpZ" class="token"><code>eatAndDrinkCoffeeTea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment that sells drinks, such as coffee and tea, as well as refreshments.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let eatAndDrinkCoffeeTea: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21goingOutEntertainmentSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-goingOutEntertainment" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21goingOutEntertainmentSSvpZ" class="token"><code>goingOutEntertainment</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places commonly associated with entertainment, such as bars, cinemas, theatres, casinos and night clubs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let goingOutEntertainment: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17goingOutNightlifeSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-goingOutNightlife" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17goingOutNightlifeSSvpZ" class="token"><code>goingOutNightlife</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment that provides evening entertainment and usually serves alcoholic beverages.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let goingOutNightlife: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC14goingOutCinemaSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-goingOutCinema" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC14goingOutCinemaSSvpZ" class="token"><code>goingOutCinema</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment that shows movies through screen projection.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let goingOutCinema: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27goingOutTheatreMusicCultureSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-goingOutTheatreMusicCulture" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27goingOutTheatreMusicCultureSSvpZ" class="token"><code>goingOutTheatreMusicCulture</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment where various types of performing arts are presented.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let goingOutTheatreMusicCulture: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC30goingOutGamblingLotteryBettingSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-goingOutGamblingLotteryBetting" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC30goingOutGamblingLotteryBettingSSvpZ" class="token"><code>goingOutGamblingLotteryBetting</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment that provides gambling entertainment.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let goingOutGamblingLotteryBetting: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC16sightsAndMuseumsSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-sightsAndMuseums" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC16sightsAndMuseumsSSvpZ" class="token"><code>sightsAndMuseums</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places of special interest, such as common tourist attractions, museums and places of worship.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let sightsAndMuseums: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC24sightsLandmarkAttractionSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-sightsLandmarkAttraction" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC24sightsLandmarkAttractionSSvpZ" class="token"><code>sightsLandmarkAttraction</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A designated area of special interest to tourists.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let sightsLandmarkAttraction: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC12sightsMuseumSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-sightsMuseum" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC12sightsMuseumSSvpZ" class="token"><code>sightsMuseum</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let sightsMuseum: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC015sightsReligiousB0SSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-sightsReligiousPlace" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC015sightsReligiousB0SSvpZ" class="token"><code>sightsReligiousPlace</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment special religious significance or where religious services are held.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let sightsReligiousPlace: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC22naturalAndGeographicalSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-naturalAndGeographical" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC22naturalAndGeographicalSSvpZ" class="token"><code>naturalAndGeographical</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for natural or man-made areas of regional importance, such as bodies of water, mountains, forested areas and other geographic areas.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let naturalAndGeographical: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC33naturalAndGeographicalBodyOfWaterSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-naturalAndGeographicalBodyOfWater" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC33naturalAndGeographicalBodyOfWaterSSvpZ" class="token"><code>naturalAndGeographicalBodyOfWater</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A natural and geographical feature of the earth’s surface that is covered with water, such as a lake, river, stream or ocean.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let naturalAndGeographicalBodyOfWater: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC36naturalAndGeographicalMountainOrHillSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-naturalAndGeographicalMountainOrHill" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC36naturalAndGeographicalMountainOrHillSSvpZ" class="token"><code>naturalAndGeographicalMountainOrHill</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A natural and geographical feature that is higher than the surrounding land.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let naturalAndGeographicalMountainOrHill: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC37naturalAndGeographicalUnderseaFeatureSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-naturalAndGeographicalUnderseaFeature" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC37naturalAndGeographicalUnderseaFeatureSSvpZ" class="token"><code>naturalAndGeographicalUnderseaFeature</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A natural or artificial feature that is below sea level.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let naturalAndGeographicalUnderseaFeature: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC49naturalAndGeographicalForestHealthOtherVegetationSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-naturalAndGeographicalForestHealthOtherVegetation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC49naturalAndGeographicalForestHealthOtherVegetationSSvpZ" class="token"><code>naturalAndGeographicalForestHealthOtherVegetation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A dense growth of trees, open uncultivated land or other large masses of vegetation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let naturalAndGeographicalForestHealthOtherVegetation: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27naturalAndGeographicalOtherSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-naturalAndGeographicalOther" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27naturalAndGeographicalOtherSSvpZ" class="token"><code>naturalAndGeographicalOther</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let naturalAndGeographicalOther: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC9transportSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-transport" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC9transportSSvpZ" class="token"><code>transport</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places commonly associated with pedestrian and cargo transport facilities, including airports, rail yards and seaports.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let transport: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC16transportAirportSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-transportAirport" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC16transportAirportSSvpZ" class="token"><code>transportAirport</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let transportAirport: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC15transportPublicSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-transportPublic" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC15transportPublicSSvpZ" class="token"><code>transportPublic</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A facility for travelers who are travelling between stops on public transport.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let transportPublic: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC14transportCargoSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-transportCargo" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC14transportCargoSSvpZ" class="token"><code>transportCargo</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A facility that handles some aspect of the transportation of cargo freight.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let transportCargo: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17transportRestAreaSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-transportRestArea" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17transportRestAreaSSvpZ" class="token"><code>transportRestArea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment along a motorway (controlled access road) that provides restrooms and parking.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let transportRestArea: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC13accommodationSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-accommodation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC13accommodationSSvpZ" class="token"><code>accommodation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers, such as hotels, motels, resorts, cruise ships and campgrounds.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let accommodation: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC23accommodationHotelMotelSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-accommodationHotelMotel" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC23accommodationHotelMotelSSvpZ" class="token"><code>accommodationHotelMotel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that provides lodging or temporary living quarters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let accommodationHotelMotel: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC20accommodationLodgingSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-accommodationLodging" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC20accommodationLodgingSSvpZ" class="token"><code>accommodationLodging</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that provides lodging to the public generally without room service.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let accommodationLodging: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17leisureAndOutdoorSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-leisureAndOutdoor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17leisureAndOutdoorSSvpZ" class="token"><code>leisureAndOutdoor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places that are designated for sports, recreation, parking, beaches and other leisure and outdoor activities.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let leisureAndOutdoor: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC24leisureOutdoorRecreationSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-leisureOutdoorRecreation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC24leisureOutdoorRecreationSSvpZ" class="token"><code>leisureOutdoorRecreation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Public land preserved and maintained for recreational use.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let leisureOutdoorRecreation: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC12leisureOtherSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-leisureOther" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC12leisureOtherSSvpZ" class="token"><code>leisureOther</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A park that contains rides and/or other entertainment which may be based on a central theme.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let leisureOther: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC8shoppingSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shopping" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC8shoppingSSvpZ" class="token"><code>shopping</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places where consumer goods are commonly sold, such as clothing stores, grocery stores, hardware stores and other types of shopping centers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shopping: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC24shoppingConvenienceStoreSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingConvenienceStore" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC24shoppingConvenienceStoreSSvpZ" class="token"><code>shoppingConvenienceStore</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingConvenienceStore: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC19shoppingMallComplexSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingMallComplex" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC19shoppingMallComplexSSvpZ" class="token"><code>shoppingMallComplex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A complex of businesses that are co-located and share common services.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingMallComplex: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC23shoppingDepartmentStoreSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingDepartmentStore" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC23shoppingDepartmentStoreSSvpZ" class="token"><code>shoppingDepartmentStore</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that sells a wide variety of merchandise that is organized by product or service departments.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingDepartmentStore: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC20shoppingFoodAndDrinkSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingFoodAndDrink" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC20shoppingFoodAndDrinkSSvpZ" class="token"><code>shoppingFoodAndDrink</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that sells specialty products of a particular type of food or beverage.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingFoodAndDrink: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC25shoppingDrugstorePharmacySSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingDrugstorePharmacy" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC25shoppingDrugstorePharmacySSvpZ" class="token"><code>shoppingDrugstorePharmacy</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that sells medications, toiletry items and other retail cosmetics.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingDrugstorePharmacy: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC19shoppingElectronicsSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingElectronics" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC19shoppingElectronicsSSvpZ" class="token"><code>shoppingElectronics</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that sells consumer electronics and electronic entertainment equipment.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingElectronics: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27shoppingHardwareHouseGardenSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingHardwareHouseGarden" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27shoppingHardwareHouseGardenSSvpZ" class="token"><code>shoppingHardwareHouseGarden</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that sells crafts, gardening, remodeling, or decorating items for the home.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingHardwareHouseGarden: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17shoppingBookstoreSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingBookstore" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17shoppingBookstoreSSvpZ" class="token"><code>shoppingBookstore</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that sells books, magazines and other reading material.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingBookstore: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC29shoppingClothingAndAccesoriesSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingClothingAndAccesories" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC29shoppingClothingAndAccesoriesSSvpZ" class="token"><code>shoppingClothingAndAccesories</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that sells apparel items, garments or fashion accessories for men, women, and children.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingClothingAndAccesories: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21shoppingConsumerGoodsSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingConsumerGoods" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21shoppingConsumerGoodsSSvpZ" class="token"><code>shoppingConsumerGoods</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that sells a variety of products targeted to consumers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingConsumerGoods: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21shoppingHairAndBeautySSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shoppingHairAndBeauty" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21shoppingHairAndBeautySSvpZ" class="token"><code>shoppingHairAndBeauty</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A business that provides hair styling and personal appearance services. Places in this category may also sell hair products and other related cosmetic items.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shoppingHairAndBeauty: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC19businessAndServicesSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServices" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC19businessAndServicesSSvpZ" class="token"><code>businessAndServices</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places that provide professional services to other businesses, such as printing, photocopying, graphic design, marketing, advertising and other general business services.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServices: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC26businessAndServicesBankingSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesBanking" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC26businessAndServicesBankingSSvpZ" class="token"><code>businessAndServicesBanking</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that specialize in the maintenance, lending, exchange, or issuance of money.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesBanking: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC22businessAndServicesAtmSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesAtm" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC22businessAndServicesAtmSSvpZ" class="token"><code>businessAndServicesAtm</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesAtm: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC28businessAndServicesMoneyCashSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesMoneyCash" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC28businessAndServicesMoneyCashSSvpZ" class="token"><code>businessAndServicesMoneyCash</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that provide money related services.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesMoneyCash: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC37businessAndServicesCommunicationMediaSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesCommunicationMedia" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC37businessAndServicesCommunicationMediaSSvpZ" class="token"><code>businessAndServicesCommunicationMedia</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that provide communication services.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesCommunicationMedia: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC29businessAndCommercialServicesSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndCommercialServices" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC29businessAndCommercialServicesSSvpZ" class="token"><code>businessAndCommercialServices</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that provide a service or product for use by other businesses.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndCommercialServices: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27businessAndServicesIndustrySSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesIndustry" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27businessAndServicesIndustrySSvpZ" class="token"><code>businessAndServicesIndustry</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that employ people in and around the city in which it is located.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesIndustry: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC38businessAndServicesPoliceFireEmergencySSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesPoliceFireEmergency" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC38businessAndServicesPoliceFireEmergencySSvpZ" class="token"><code>businessAndServicesPoliceFireEmergency</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Municipal emergency services.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesPoliceFireEmergency: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27businessAndConsumerServicesSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndConsumerServices" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC27businessAndConsumerServicesSSvpZ" class="token"><code>businessAndConsumerServices</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An organization that provides consumer services for a variety of products for used by the public.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndConsumerServices: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC29businessAndServicesPostOfficeSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesPostOffice" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC29businessAndServicesPostOfficeSSvpZ" class="token"><code>businessAndServicesPostOffice</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesPostOffice: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC37businessAndServicesTouristInformationSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesTouristInformation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC37businessAndServicesTouristInformationSSvpZ" class="token"><code>businessAndServicesTouristInformation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that provide a variety of information for visiting tourists, such as event schedules, lodging/accommodations, restaurants, attractions and more.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesTouristInformation: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC33businessAndServicesFuelingStationSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesFuelingStation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC33businessAndServicesFuelingStationSSvpZ" class="token"><code>businessAndServicesFuelingStation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that sell fuel for vehicles, such as petrol, electricity etc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesFuelingStation: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesPetrolGasolineStation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC40businessAndServicesPetrolGasolineStationSSvpZ" class="token"><code>businessAndServicesPetrolGasolineStation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that sell fuel, oil, and other motoring supplies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesPetrolGasolineStation: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesEvChargingStation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC36businessAndServicesEvChargingStationSSvpZ" class="token"><code>businessAndServicesEvChargingStation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that provide recharging services for electric vehicles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesEvChargingStation: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC33businessAndServicesCarDealerSalesSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesCarDealerSales" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC33businessAndServicesCarDealerSalesSSvpZ" class="token"><code>businessAndServicesCarDealerSales</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that sell new automobiles and motorcycles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesCarDealerSales: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC028businessAndServicesCarRepairF0SSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesCarRepairServices" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC028businessAndServicesCarRepairF0SSvpZ" class="token"><code>businessAndServicesCarRepairServices</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that provide automotive repair services.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesCarRepairServices: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC28businessAndServicesCarRentalSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesCarRental" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC28businessAndServicesCarRentalSSvpZ" class="token"><code>businessAndServicesCarRental</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Businesses that rent or lease automobiles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesCarRental: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC34businessAndServicesTruckSemiDealerSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-businessAndServicesTruckSemiDealer" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC34businessAndServicesTruckSemiDealerSSvpZ" class="token"><code>businessAndServicesTruckSemiDealer</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Business that sell or service trucks and tractor trailers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let businessAndServicesTruckSemiDealer: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC10facilitiesSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilities" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC10facilitiesSSvpZ" class="token"><code>facilities</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places associated with specialized facilities, such as sports venues, government buildings, health care centers and other types of facilities.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilities: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC28facilitiesHospitalHealthcareSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilitiesHospitalHealthcare" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC28facilitiesHospitalHealthcareSSvpZ" class="token"><code>facilitiesHospitalHealthcare</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Facilities that include dental offices, hospitals, nursing homes and other health care-related services.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilitiesHospitalHealthcare: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC30facilitiesGovernmentCommunittySSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilitiesGovernmentCommunitty" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC30facilitiesGovernmentCommunittySSvpZ" class="token"><code>facilitiesGovernmentCommunitty</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A Place where government services are provided.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilitiesGovernmentCommunitty: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC19facilitiesEducationSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilitiesEducation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC19facilitiesEducationSSvpZ" class="token"><code>facilitiesEducation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Facilities that are used for educational purposes including training, coaching, universities and more.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilitiesEducation: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC16facilitiesSchoolSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilitiesSchool" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC16facilitiesSchoolSSvpZ" class="token"><code>facilitiesSchool</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Educational facilities that include primary schools, secondary schools and more.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilitiesSchool: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17facilitiesLibrarySSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilitiesLibrary" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17facilitiesLibrarySSvpZ" class="token"><code>facilitiesLibrary</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Facilities that offer books, periodicals, audio, video and other material for public use.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilitiesLibrary: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21facilitiesEventSpacesSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilitiesEventSpaces" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21facilitiesEventSpacesSSvpZ" class="token"><code>facilitiesEventSpaces</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An area or facility used for the hosting of fairs and conventions.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilitiesEventSpaces: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17facilitiesParkingSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilitiesParking" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17facilitiesParkingSSvpZ" class="token"><code>facilitiesParking</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Area or building used for parking cars.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilitiesParking: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21facilitiesVenueSportsSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilitiesVenueSports" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC21facilitiesVenueSportsSSvpZ" class="token"><code>facilitiesVenueSports</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A facility used for individual and team sports including recreational sports.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilitiesVenueSports: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC15facilitiesOtherSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-facilitiesOther" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC15facilitiesOtherSSvpZ" class="token"><code>facilitiesOther</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let facilitiesOther: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17areasAndBuildingsSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-areasAndBuildings" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC17areasAndBuildingsSSvpZ" class="token"><code>areasAndBuildings</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Top level category for places that are owned, operated or managed by municipalities, such as cities, towns, villages, boroughs and shires.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let areasAndBuildings: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC31areasAndBuildingsOutdoorComplexSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-areasAndBuildingsOutdoorComplex" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC31areasAndBuildingsOutdoorComplexSSvpZ" class="token"><code>areasAndBuildingsOutdoorComplex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Outdoor areas or complexes with designations for specific businesses or interests.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let areasAndBuildingsOutdoorComplex: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC33areasAndBuildingsResidentalOfficeSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-areasAndBuildingsResidentalOffice" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC33areasAndBuildingsResidentalOfficeSSvpZ" class="token"><code>areasAndBuildingsResidentalOffice</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Areas and buildings designated for residential or office use.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let areasAndBuildingsResidentalOffice: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC2idSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC2idSSvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Place category ID.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC4nameSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-name" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-placecategory#sdk-for-ios-navigate-s-7heresdk13PlaceCategoryC4nameSSSgvp" class="token"><code>name</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Localised place category name. It is available only when when `PlaceCategory` is obtained from <a href="sdk-for-ios-navigate-classes-place">`Place`</a>. That means that when `PlaceCategory` is constructed directly by the client, `name` is always `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

