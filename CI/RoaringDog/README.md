this repo is for portal e2e test

linux OS:
git clone ssh://aohang@192.168.0.100:8011/RoaringDog && scp -p -P 8011 aohang@192.168.0.100:hooks/commit-msg RoaringDog/.git/hooks/
git clone ssh://aohang@192.168.0.100:8011/erlang && scp -p -P 8011 aohang@192.168.0.100:hooks/commit-msg erlang/.git/hooks/

step 1:
prepare image: need to do at first time or the Dockfile changed
cd RoaringDog
docker build -t cypress/forci:v1 ./

step 2 
run test:
erlang and RoaringDog must be in same directoy,as below:
sdn@web_test:~/aohang$ ls
erlang  RoaringDog

cd ~/aohang
sudo docker run -i -v $PWD:/e2e -w /e2e  --name e2etest cypress/forci:v3  sh -c "ln -s /usr/local/lib/node_modules /e2e/RoaringDog; cd RoaringDog;cypress run --record --key 4dff0eb4-3795-4783-a925-60a5a8e4f619 --spec "cypress/integration/testcase/sdwan-site-test.js" ; cd /e2e/RoaringDog/cypress/results/; npx mochawesome-merge 'mochawesome*.json' > report.json;npx marge report.json;rm -rf /e2e/RoaringDog/node_modules"

cypress run docker with GUI(testRunner)
first start x server on host with GUI
then run script as bellow:
 sh runtestWithGUI.sh 192.168.0.191:0.0

cat runtestWithGUI.sh
export DISPLAY=$1
sudo rm RoaringDog/cypress/results -rf
sudo docker rm -f e2etest;sudo docker run -itd -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD:/e2e -w /e2e --shm-size=1g --name e2etest harbor.netgrounder.com:800/cypress/forci:latest  sh -c "ln -s /usr/local/lib/node_modules e2e/RoaringDog;bash"
sudo docker exec -it e2etest sh -c 'cd RoaringDog;cypress open --project ./'