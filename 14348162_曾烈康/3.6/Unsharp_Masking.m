function Unsharp_Masking()
    close all
    fi=imread('Fig3.43(a).jpg');
    figure,imshow(fi),title('ԭʼͼ��');

    im = double(fi);
    mask = [1/9 1/9 1/9;1/9 1/9 1/9;1/9 1/9 1/9];%mask��ʾ��ģ����
    %c=conv2(fi,w,'same');              %����ϵͳ�Դ��ľ������ʵ��
    c = BlurFilter(im,mask);
    figure,imshow(c),title('ģ��ͼ��');
    imwrite(c,'Fig3.43(a)blur.jpg');
    gmask = im-c;
    figure,imshow(gmask),title('ģ��ͼ��');
    imwrite(gmask,'Fig3.43(a)mask.jpg');
    
    A=[1,2,3,5,10,20,30,50];                 %A����������õĲ��Գ���
    for i = 1:length(A)
        g = im*(A(i)-1)+gmask;
        g = uint8(g);                   %ÿ�ξ���ӡ��ͼ��
        figure(i),imshow(g),title(['����ͼ�� A=',num2str(A(i))]);
        saveas(i,['Fig3.43(a)_A',num2str(A(i)),'.jpg']);
    end
    
function imGau = BlurFilter(fi,mask)    %�����˲���ľ���
    im = double(fi);
    [m,n] = size(fi);
    imGau = zeros(m,n);
    for x = 2:m-1           %��ÿ�����ص㣬����ģ�����Ȩ�����Χ������ֵ
        for y = 2:n-1
            imGau(x,y)=im(x-1,y-1)*mask(1,1)+im(x-1,y)*mask(1,2)+im(x-1,y+1)*mask(1,3)...          
                +im(x,y-1)*mask(2,1)+im(x,y)*mask(2,2)+im(x,y+1)*mask(2,3)...        
                +im(x+1,y-1)*mask(3,1)+im(x+1,y)*mask(3,2)+im(x+1,y+1)*mask(3,3);
        end
    end