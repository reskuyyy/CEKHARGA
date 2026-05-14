export default async function handler(req, res){

  const {
    storeId,
    rack
  } = req.query;

  const url =
  `https://app.alfastore.co.id/prd/api/mob/tablet/productinfo/CheckPerRack/?storeId=${storeId}&rack=${rack}`;

  try{

    const response =
    await fetch(url, {

      headers:{
        'User-Agent':'Mozilla/5.0'
      }

    });

    const text =
    await response.text();

    // kirim raw response
    res.status(200).send(text);

  }catch(err){

    res.status(500).json({

      error:'Fetch gagal',

      detail:err.message

    });

  }

}
